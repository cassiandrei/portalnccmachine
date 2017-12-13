# coding=utf-8

from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^alterar-senha/$', views.update_password, name='update_password'),
    url(r'^registro/$', views.register, name='register'),
    url(r'^cadastrar/(?P<username>\w+)/(?P<token>[0-9]+)$', views.cadastrar, name='cadastro'),
]
