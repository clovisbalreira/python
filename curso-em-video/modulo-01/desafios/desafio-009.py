# Faça um programa que leia um numéro Inteiro qualquer e mostre na tela sua tabuada
numero = int(input('Digite um número: '))
m1 = numero * 1
m2 = numero * 2
m3 = numero * 3
m4 = numero * 4
m5 = numero * 5
m6 = numero * 6
m7 = numero * 7 
m8 = numero * 8
m9 = numero * 9
m10 = numero * 10
print('A tabuada de {}'.format(numero))
print('=' * 12)
print('{} * {:2} = {}'.format(numero, 1 ,m1))
print('{} * {:2} = {}'.format(numero, 2 ,m2))
print('{} * {:2} = {}'.format(numero, 3 ,m3))
print('{} * {:2} = {}'.format(numero, 4 ,m4))
print('{} * {:2} = {}'.format(numero, 5 ,m5))
print('{} * {:2} = {}'.format(numero, 6 ,m6))
print('{} * {:2} = {}'.format(numero, 7 ,m7))
print('{} * {:2} = {}'.format(numero, 8 ,m8))
print('{} * {:2} = {}'.format(numero, 9 ,m9))
print('{} * {} = {}'.format(numero, 10 ,m10))
print('=' * 12)