# Importanto a função do arquivo calculadora/__init__.py
import sys
import os
sys.path.insert(0, os.getcwd())
from calculadora import calcule

# Executando a aplicação
calcule()