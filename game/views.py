from django.shortcuts import render
from game.forms import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'game/index.html')

def gameregister(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jogo cadastrado com sucesso')
        else:
            messages.error(request, 'Dados invalidos')
    return render(request, 'game/add.html', {'form': form})