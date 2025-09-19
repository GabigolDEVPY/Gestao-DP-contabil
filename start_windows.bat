@echo off

IF NOT EXIST ".venv" (
    echo Criando Ambiente Virtual...
    python -m venv .venv
    call .venv\Scripts\activate
    echo Instalando Depêndencias...
    pip install -r requirements.txt
) ELSE (
    echo Ativando Servidor...
    call .venv\Scripts\activate
)

python wsgi.py
