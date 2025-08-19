# Adicione ao modulo moeda.py criado no desafios anteriores uma função chamada resumo(),que mostre na tela algumas informações geradas pela funções que já temos no módulo criado até aqui.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import moeda
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 30)