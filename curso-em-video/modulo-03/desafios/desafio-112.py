# Dentro do pacote utilidadesCev que criamos no dessafio 111 temos um módulo chamado dado. Crie uma fução chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com um validação de dados para aceitars apenas valore que seja monetários.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos.utilidadesCev import moeda
from modulos.utilidadesCev import dado
p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 80, 35) 