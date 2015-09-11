from django.shortcuts import render
from SC import settings
from .models import *
from twython import Twython
from django.http import HttpResponse
import oauth2 as oauth
import cgi
from django.http import HttpResponseRedirect

consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY,
                          settings.TWITTER_CONSUMER_SECRET)
client = oauth.Client(consumer)
request_token_url = 'https://api.twitter.com/oauth/request_token'
authenticate_url = 'https://api.twitter.com/oauth/authenticate'

def twitter_login(request):

     # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    # Step 2. Store the request token in a session for later use.
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Step 3. Redirect the user to the authentication URL.
    url = "%s?oauth_token=%s" % (authenticate_url,
        request.session['request_token']['oauth_token'])

    return HttpResponseRedirect(url)


def logueado_twitter(request, redirect_url=settings.LOGIN_REDIRECT_URL):
    """
        A user gets redirected here after hitting Twitter and authorizing your
        app to use their data.

        ***
            This is the view that stores the tokens you want
            for querying data. Pay attention to this.
        ***
    """
    # Now that we've got the magic tokens back from Twitter, we need to exchange
    # for permanent ones and store them...

    twitter = Twython(
        app_key=settings.TWITTER_CONSUMER_KEY,
        app_secret=settings.TWITTER_CONSUMER_SECRET,
        oauth_token=request.session['request_token']['oauth_token'],
        oauth_token_secret=request.session['request_token']['oauth_token_secret'],
    )

    # Retrieve the tokens we want...
    try:
        print('autorizando')
        authorized_tokens = twitter.get_authorized_tokens(request.GET['oauth_verifier'])
        print('AUTORIZADO!!!!!')
    except BaseException:
        request.session['fallo_login'] = "Tiene que acpetar la politica de la aplicacion."
        return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')
    usuario = UsuarioTwitter.objects.filter(id_twitter=authorized_tokens["user_id"])
    if usuario is not None and len(usuario) > 0:
        request.session["fallo_login"] = "Ya tiene esta cuenta asociada."
        usuario = usuario[0]
        usuario.screen_name = authorized_tokens['screen_name']
        usuario.token = authorized_tokens['oauth_token']
        usuario.token_secret = authorized_tokens['oauth_token_secret']
        return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')

    # If they already exist, grab them, login and redirect to a page displaying stuff.
    try:
        if User.objects.filter(username=authorized_tokens['screen_name']).exists():
            user = User.objects.get(username=authorized_tokens['screen_name'])
        else:
            user = User.objects.get(username="luis")

        usuario = UsuarioTwitter(
            user=user,
            screen_name=authorized_tokens['screen_name'],
            token=authorized_tokens['oauth_token'],
            token_secret=authorized_tokens['oauth_token_secret'],
            id_twitter=authorized_tokens['user_id'],
        )
        usuario.save()
        usuario_monitorizar.save()
        request.session['oauth_token'] = authorized_tokens['oauth_token']
        request.session['oauth_token_secret'] = authorized_tokens['oauth_token_secret']
    except BaseException:
        request.session['fallo_login'] = "Ha fallado la conexion con la BBDD, contacte con el administrador"
        return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')

    request.session['networks_agregados'] = Network.objects.filter(cuenta=request.session['cuenta']).__len__()
    return HttpResponse('<script type="text/javascript">window.close(); window.parent.location.href = "/";</script>')
