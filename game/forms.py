# coding=utf-8

from django import forms
from game.models import Game
import zipfile


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['user']

    def clean_arquivo(self):
        file = self.cleaned_data['arquivo']
        if file.size > 314572800:
            raise forms.ValidationError("Tamanho do arquivo excedido")
        if file.name.split('.')[1] != 'zip':
            raise forms.ValidationError("Use formato ZIP para enviar o jogo")
        with zipfile.ZipFile(file, 'r') as game_zip:
            if 'run.sh' not in game_zip.namelist():
                raise forms.ValidationError("O arquivo ZIP deve conter um arquivo run.sh")
        return file
