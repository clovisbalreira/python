# Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobra() e metade()
# Faça também um programa que importe esse módulo e use alguma dessas funções

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'A dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% {p} é {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13% de {p} é {moeda.diminuir(p, 13)}')