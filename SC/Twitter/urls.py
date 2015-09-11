from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logueado_twitter/?$', views.logueado_twitter, name="twitter_callback"),
    url(r'^login/?$', views.twitter_login),
]
