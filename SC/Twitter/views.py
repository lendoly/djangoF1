from django.shortcuts import render
import oauth2
from SC import settings
import cgi
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UsuarioTwitter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

consumer = oauth2.Consumer(settings.TWITTER_CONSUMER_KEY,
                           settings.TWITTER_CONSUMER_SECRET)
client = oauth2.Client(consumer)


request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'

# This is the slightly different URL used to authenticate/authorize.
authenticate_url = 'https://api.twitter.com/oauth/authenticate'


# Create your views here.
def twitter_login(request):

    # Step 1. Get a request token from Twitter.
    resp, content = client.request(request_token_url, "GET")
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    # Step 2. Store the request token in a session for later use.
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    # Step 3. Redirect the user to the authentication URL.
    context = {'url': authenticate_url,
               'token': request.session['request_token']['oauth_token']}
    return render(request, 'twitter/index.html', context)


@login_required
def twitter_logout(request):
    # Log a user out using Django's logout function and redirect them
    # back to the homepage.
    logout(request)
    return HttpResponseRedirect('/')


def twitter_authenticated(request):
    print request.GET
    # pin = request.GET.get('pin')
    # if not pin:
        # return render(request, 'twitter/pin.html', {})

    # Step 1. Use the request token in the session to build a new client.

    token = oauth2.Token(request.session['request_token']['oauth_token'],
                         request.session['request_token']
                         ['oauth_token_secret'])
    token.set_verifier(request.GET.get('oauth_verifier'))
    # token.set_verifier(request.GET.get('pin'))
    client = oauth2.Client(consumer, token)

    # Step 2. Request the authorized access token from Twitter.
    resp, content = client.request(access_token_url, method="GET",
                                   body="", headers=None)
    print resp
    print content
    if resp['status'] != '200':
        raise Exception("Invalid response from Twitter.")

    """
    This is what you'll get back from Twitter. Note that it includes the
    user's user_id and screen_name.
    {
        'oauth_token_secret': 'IcJXPiJh8be3BjDWW50uCY31chyhsMHEhqJVsphC3M',
        'user_id': '120889797',
        'oauth_token': '120889797-H5zNnM3qE0iFoTTpNEHIz3noL9FKzXiOxwtnyVOD',
        'screen_name': 'heyismysiteup'
    }
    """
    access_token = dict(cgi.parse_qsl(content))

    # Step 3. Lookup the user or create them if they don't exist.
    try:
        user = User.objects.get(username=access_token['screen_name'])
    except User.DoesNotExist:
        # When creating the user I just use their screen_name@twitter.com
        # for their email and the oauth_token_secret for their password.
        # These two things will likely never be used. Alternatively, you
        # can prompt them for their email here. Either way, the password
        # should never be used.
        user = User.objects.create_user(access_token['screen_name'],
                                        '%s@twitter.com' % access_token[
                                            'screen_name'],
                                        access_token['oauth_token_secret'])

        # Save our permanent token and secret for later.
        usuario_twitter = UsuarioTwitter()
        usuario_twitter.user = user
        usuario_twitter.token = access_token['oauth_token']
        usuario_twitter.token_secret = access_token['oauth_token_secret']
        usuario_twitter.screen_name = access_token['screen_name']
        usuario_twitter.id_twitter = access_token['user_id']
        usuario_twitter.save()

    # Authenticate the user and log them in using Django's pre-built
    # functions for these things.
    user = authenticate(username=access_token['screen_name'],
                        password=access_token['oauth_token_secret'])
    login(request, user)

    return HttpResponseRedirect('/')
