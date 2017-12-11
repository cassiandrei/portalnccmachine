#!/bin/bash

# Script utilizado para rodar a aplicação localmente
# necessario pacotes python3 e pip3 instalados

#instalando pacotes pip do projeto
pip3 install -r requirements.txt

#migrações do banco
python3 manage.py makemigrations

#aplicando migrações
python3 manage.py migrate

# executa o navegador
python3 -m webbrowser -t "http://127.0.0.1:8000"

# inicia a aplicação no localhost
python3 manage.py runserver