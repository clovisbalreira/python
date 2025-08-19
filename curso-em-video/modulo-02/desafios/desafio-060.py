from math import factorial
# Faça um programa que leia número qualquer e mostre o seu fatorial
# ex: 5! = 5X4X3X2X1=120 
numero = int(input('Digite um número: '))
c = numero
f = 1
print('{}! = '.format(numero, numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

f = factorial(numero)
print('O factorial de {} é {}'.format(numero, f))