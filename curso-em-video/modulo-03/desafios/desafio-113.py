# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a posibilidade da digitação de um número de tipo inválido.Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import numeros

n = numeros.leiaInt('Digite um inteiro: ')
r = numeros.leiaFloat('Digite um Real: ')
print(f'O valor digitado foi {n} e o real {r}')