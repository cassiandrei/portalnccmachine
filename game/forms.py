# coding=utf-8

from django import forms
from game.models import Game
from django.contrib import messages


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def is_valid(self):
        valid = super(GameForm, self).is_valid()
        if not valid:
            return valid

        file_object = self.cleaned_data.get('arquivo')
        if file_object.size > 314572800:
            self.errors['arquivo'] = 'Tamanho da foto excedido'
            return False
        if file_object.name.split('.')[1] != 'zip':
            self.errors['arquivo'] = 'Use formato ZIP para enviar o jogo'
            return False
