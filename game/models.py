from django.db import models
from accounts.models import User
# Create your models here.

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, help_text='Nome do Jogo', unique=True)
    autores = models.TextField(max_length=500, help_text='Digite seus autores')
    versao = models.CharField(max_length=30, help_text='Versão do jogo')
    descricao = models.TextField(max_length=500)

    def arquivoname(self, filename):
        return str(self.nome) + '.' + filename.split('.')[-1]

    arquivo = models.FileField(help_text='zip do jogo', upload_to=arquivoname)