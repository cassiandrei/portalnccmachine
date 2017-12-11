from django.db import models

# Create your models here.
class Game(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Jogo')
    autores = models.TextField(max_length=500, help_text='Digite seus autores')
    capa = models.ImageField(help_text='Imagem de capa do Game', blank=True, null=True)
    miniatura = models.ImageField(help_text='Foto de miniatura', blank=True, null=True)
    screen = models.ImageField(help_text='PrintSCreen do GamePlay', blank=True, null=True)
    descricao = models.TextField(max_length=500)