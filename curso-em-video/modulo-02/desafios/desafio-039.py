# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Digite o ano que você nasceu: '))
idade = anoAtual - anoNascimento
print('Estamos no ano {} e você nasceu no ano {}\nVocê tem {} anos'.format(anoAtual, anoNascimento, idade))
if anoAtual - anoNascimento == 18:
    print('Esse ano você vai se alistar')
elif anoAtual - anoNascimento < 18:
    print('falta {} ano(s) para você se alistar\nO ano {} é para você se alistar'.format(18 - (anoAtual - anoNascimento), anoAtual + (18 - (anoAtual - anoNascimento))))
else:
    print('Seu tempo de alistamento passou a {} anos\nO ano era {} para você se alistar'.format((anoAtual - anoNascimento) - 18, anoAtual - (idade - 18)))


