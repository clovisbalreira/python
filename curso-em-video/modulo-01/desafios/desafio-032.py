from datetime import date
# Faça um programa que leia o ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Digite o ano ( se quiser analizar o ano atual digite 0 ) '))
if ano == 0:
    ano = date.today().year
if ano %  4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))