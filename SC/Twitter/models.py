from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UsuarioTwitter (models.Model):

    user = models.ForeignKey(User)
    id_twitter = models.IntegerField()
    token = models.TextField()
    token_secret = models.TextField()
    screen_name = models.TextField()
