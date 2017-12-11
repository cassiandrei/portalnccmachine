# coding=utf-8

from django import forms
from game.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ['user']

    def clean_recipients(self):
        file = self.cleaned_data['arquivo']
        if file.size > 314572800:
            raise forms.ValidationError("Tamanho da foto excedido")
        if file.name.split('.')[1] != 'zip':
            raise forms.ValidationError("Use formato ZIP para enviar o jogo")
        return file