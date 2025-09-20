#!/bin/bash

if [ ! -d ".venv" ]; then
    echo "Criando Ambiente Virtual..."
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Instalando Dependências..."
    pip install -r requirements.txt
else
    echo "Ativando Servidor..."
    source .venv/bin/activate
fi

python3 wsgi.py
