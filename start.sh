#!/bin/bash

# Script universal para iniciar a aplicação
echo "🔍 Detectando sistema operacional..."

# Cria diretório se não existir
mkdir -p database

if [ "$OSTYPE" = "msys" ] || [ "$OSTYPE" = "win32" ] || [ "$OSTYPE" = "cygwin" ]; then
    echo "🐢 Windows detectado"
    source env/Scripts/activate
else
    echo "🐧 Linux/Unix detectado"
    source env/bin/activate
fi

echo "🚀 Iniciando servidor Flask..."
flask run --host 0.0.0.0 --port 5000 --reload

# Esse script serve para:
# 1 - Ativar e entrar no bash do ambiente virtual
# 2 - Inicializar o servidor
# Para executar o start.sh basta abrir o terminal e executar
# source start.sh