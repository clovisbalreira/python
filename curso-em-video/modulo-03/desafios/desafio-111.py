# Crie um pagode chamado utilidadesCev que tenha dois módulos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import moeda
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)