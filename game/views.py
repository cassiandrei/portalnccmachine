from django.shortcuts import render
from game.forms import *
from django.contrib import messages
from django.shortcuts import redirect
from .models import Game
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
            return redirect('accounts:index')
        else:
            messages.error(request, 'Dados invalidos')
    return render(request, 'game/add.html', {'form': form})

def lista_jogos(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'game/lista_jogos.html', context)

def remove(request, id):
    Game.objects.get(id=id).delete()
    messages.success(request, 'Jogo Removido')
    return redirect('accounts:index')