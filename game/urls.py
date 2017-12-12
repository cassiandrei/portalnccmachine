# coding=utf-8

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    url(r'^adicionar$', views.gameregister, name='add'),
    url(r'^lista/$', views.lista_jogos, name='lista_jogos'),
    path('remove/<int:id>/', views.remove, name='remove'),
    url(r'^json/$', views.getAllGames, name='json'),
]
