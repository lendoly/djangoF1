from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^circuitos/$', views.circuitos, name='circuitos'),
    url(r'^circuitos/(?P<circuito_id>[0-9]+)/$', views.circuito_detail,
        name='circuito_detail'),
    url(r'^grandes_premios/$', views.grandes_premios, name='grandes_premios'),
    url(r'^grandes_premios/(?P<gran_premio_id>[0-9]+)/$', views.gran_premio,
        name='gran_premio'),

]
