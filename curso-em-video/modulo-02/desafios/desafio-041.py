from datetime import date
# A Confederação nacional de natação precisa de um programa que leia  o ano de nascimento de um atleta e mostre  sua categoria, de acordo com a idade:
# até 9 anos:Mirim
# até 14 anos:Infantil
# até 19 anos:Junior
# até 25 anos:Sênior
# Acima:Master
anoAtual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - nascimento
print('Sua idade é {} anos'.format(idade))
if idade <= 9 :
    print('Sua categoria é de mirim')
elif idade <= 14 :
    print('Sua categoria é de infantil')
elif idade <= 19 :
    print('Sua categoria é de júnior')
elif idade <= 25 :
    print('Sua categoria é de sênior')
else :
    print('Sua categoria é de master')