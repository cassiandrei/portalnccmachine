# coding=utf-8

from django.conf.urls import url

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adicionar$', views.gameregister, name='add'),
    url(r'^lista/$', views.lista_jogos, name='lista_jogos'),
]
