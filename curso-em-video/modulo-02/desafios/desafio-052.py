# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input('Digite o número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[32m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(numero, tot))
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')