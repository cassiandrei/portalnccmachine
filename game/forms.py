# coding=utf-8

from django import forms
from game.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'