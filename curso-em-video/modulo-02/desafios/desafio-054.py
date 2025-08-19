from datetime import date
# Crie um programa que leia o ano do nascimento de sete pessoas. no final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
menores = 0
maiores = 0
anoAtual = date.today().year
for c in range(1, 8):
    ano = int(input('Em que ano {}º pessoa nasceu : '.format(c)))
    idade = anoAtual - ano
    if  idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Tem {} pessoas maiores de idade'.format(maiores))
print('Tem {} pessoas menores de idade'.format(menores))