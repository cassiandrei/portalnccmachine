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
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            messages.success(request, 'Jogo cadastrado com sucesso')
        else:
            messages.error(request, 'Dados invalidos')
    return render(request, 'game/add.html', {'form': form})

def lista_jogos(request):
    return render(request, 'game/lista_jogos.html')