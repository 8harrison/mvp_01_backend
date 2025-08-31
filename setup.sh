#!/bin/bash

# Script universal para criar ambiente virtual
echo "🔍 Detectando sistema operacional..."

if [ "$OSTYPE" = "msys" ] || [ "$OSTYPE" = "win32" ] || [ "$OSTYPE" = "cygwin" ]; then
    echo "🐢 Windows detectado"
    python -m venv env
    source env/Scripts/activate
else
    echo "🐧 Linux/Unix detectado"
    python3 -m venv env
    source env/bin/activate
fi

echo "📦 Instalando dependências..."
pip install -r requirements.txt
echo "✅ Setup concluído!"


# Esse script serve para:
# 1 - Montar o ambiente virtual
# 2 - Ativar e entrar no bash do ambiente virtual
# 3 - Instalar os modulos necessários
# Para executar o setup.sh basta abrir o terminal e executar
# source setup.sh