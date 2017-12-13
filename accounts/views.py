# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse

from accounts.forms import UserAdminCreationForm
from .models import User, Token
from game.models import Game

import pyotp
import random
import string

from portal import settings


def register(request):
    if request.method == 'POST':
        username, dominio = request.POST['email'].split('@')
        if dominio == 'inf.ufsm.br':
            try:
                User.objects.get(username=username)
                messages.warning(request, 'Esse email já está cadastrado')
            except ObjectDoesNotExist:
                hotp = pyotp.HOTP('base32secret3232')
                number = random.randrange(10000)
                # Save number of auth.
                token, created = Token.objects.get_or_create(username=username)
                token.token = number
                token.save()
                key = hotp.at(number)
                # Envia email com o token para a autenticação.
                subject = "[NCC Machine] Confirmação de email ."
                url = request.build_absolute_uri(
                    reverse('accounts:cadastro', kwargs={'username': username, 'token': str(key)}))
                mensagem = "Olá, acesse a seguinte URL para continuar seu cadastro: " + url
                mfrom = settings.EMAIL_HOST_USER
                mto = [request.POST['email']]
                send_mail(subject, mensagem, mfrom, mto)
                messages.warning(request, 'Um link foi enviado para seu email para continuar o cadastro')
        else:
            messages.error(request, 'Insira um email @inf.ufsm.br')
    return render(request, 'accounts/register.html')


def cadastrar(request, token, username):
    hotp = pyotp.HOTP('base32secret3232')
    crip = Token.objects.get(username=username)
    if not hotp.verify(token, crip.token):
        messages.error(request, 'Token invalido, não foi possível fazer a confirmação de email. Tente novamente!')
        return redirect('index')
    else:
        form = UserAdminCreationForm()
        if request.method == 'POST':
            form = UserAdminCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = username
                user.email = username+'@inf.ufsm.br'
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                messages.success(request, 'Usuario criado com sucesso')
                return redirect('accounts:index')
            else:
                messages.error(request, 'Dados invalidos')
    return render(request, 'accounts/cadastro.html', {'form': form, 'token': token, 'username': username})


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()


@login_required
def index(request):
    games = Game.objects.filter(user=request.user)
    context = {'games': games}
    return render(request, 'accounts/conta.html', context)
