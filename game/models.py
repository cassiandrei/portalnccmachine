from django.db import models

# Create your models here.
class Game(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Jogo')
    autores = models.TextField(max_length=500, help_text='Digite seus autores')
    versao = models.SlugField(max_length=30, help_text='Versão do jogo')
    descricao = models.TextField(max_length=500)
    arquivo = models.FileField(help_text='zip do jogo')