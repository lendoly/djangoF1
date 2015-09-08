from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.twitter_login),
    url(r'^login/?$', views.twitter_login),
    url(r'^logout/?$', views.twitter_logout),
    url(r'^login/authenticated/?$', views.twitter_authenticated),
]
