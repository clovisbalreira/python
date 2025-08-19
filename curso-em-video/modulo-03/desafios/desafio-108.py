# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores com um valor monetário formatado

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'A dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 13))}')