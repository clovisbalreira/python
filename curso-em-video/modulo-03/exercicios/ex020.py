# modularização
# Surgiu no inicio de 60
# Sistemas ficando cada ves maiores
# Foco: dividir im programa grnade
# Foco: aumentar a legibilidade
# Foco: facilitar a manutenção

# Vantagem
# Organização de código
# Facilidade na manutenção
# Ocultação de código detalhado
# Reutilização em outros projetos

# Pacotes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from modulos import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
dobro = uteis.dobro(num)
print(f'O dobro de {num} é {dobro}')
triplo = uteis.triplo(num)
print(f'O dobro de {num} é {triplo}')