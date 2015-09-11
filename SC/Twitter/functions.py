from twitter import *
from .models import *
from SC import settings
import oauth2 as oauth

consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY,
                          settings.TWITTER_CONSUMER_SECRET)


def busca(busqueda):
    try:
        usuario = UsuarioTwitter.objects.get(screen_name='lendoly')
        t = Twitter(
            auth=OAuth(usuario.token, usuario.token_secret,
                       settings.TWITTER_CONSUMER_SECRET,
                       settings.TWITTER_CONSUMER_KEY))
        json = t.search.tweets(q=busqueda, count=100)
        parse_twiter(json)
    except BaseException, e:
        print e


def parse_twitter(json):
    for result in json['statuses']:
        print (result["text"])
        try:
            tweet = Tweet()
            tweet.id_tweet = result['id']
            tweet.mensaje = str(result["text"].encode('utf-8', 'ignore')).replace("&amp;", "&").decode('utf-8', 'ignore')
            tweet.unicodeToDate(result['created_at'])
            if Usuario_Twitter.objects.filter(id_twitter=result['user']['id']).exists():
                usuario = Usuario_Twitter.objects.get(id_twitter=result['user']['id'])
            else:
                usuario = Usuario_Twitter()
                usuario.nombre = str(result["user"]["name"].encode('utf-8', 'ignore')).decode('utf-8', 'ignore')
                usuario.screen_name = '@' + str(result["user"]["screen_name"].encode('utf-8', 'ignore')).decode('utf-8', 'ignore')
                usuario.biografia = str(result["user"]["description"].encode('utf-8', 'ignore')).decode('utf-8', 'ignore')
                usuario.id_twitter = result['user']['id']
                usuario.save()
            tweet.usuario = usuario
            tweet.save()
        except twitter.IntegrityError, e:
            print ("tweet ya existe en bbdd: ", e.message)
