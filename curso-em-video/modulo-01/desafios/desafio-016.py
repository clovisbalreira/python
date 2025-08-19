# import math
# from math import trunc
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: digite um número: 6.127
# o número 6.127  tem a parte inteira 6. 
numero = float(input('Digite um número: '))
# numeroInteiro = math.trunc(numero)
# numeroInteiro = trunc(numero)
numeroInteiro = int(numero)
print('O número {}  e sua porção inteira {}'.format(numero, numeroInteiro))