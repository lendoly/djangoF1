from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class UsuarioTwitter (models.Model):

    user = models.ForeignKey(User)
    id_twitter = models.IntegerField()
    token = models.TextField()
    token_secret = models.TextField()
    screen_name = models.TextField()


class Tweet(models.Model):

    id_tweet = models.BigIntegerField(unique=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(UsuarioTwitter)

    def unicodeToDate(self, unicode_date):
        Offset = str(unicode_date[20:25])
        dateStringWithoutOffset = str(unicode_date).replace(Offset, "")
        if str(unicode_date[4:6]).isdigit():
            dateWithTime = datetime.datetime.strptime(dateStringWithoutOffset, "%a %m %d %H:%M:%S %Y")
            trueDate = datetime.strftime(dateWithTime, "%Y-%m-%d %H:%M:%S")
        else:
            dateWithTime = datetime.strptime(dateStringWithoutOffset, "%a %b %d %H:%M:%S %Y")
            trueDate = datetime.strftime(dateWithTime, "%Y-%m-%d %H:%M:%S")

        self.fecha = trueDate


class Usuario_Twitter(models.Model):
    nombre = models.TextField()
    screen_name = models.TextField()
    biografia = models.TextField()
    id_twitter = models.BigIntegerField(unique=True)
