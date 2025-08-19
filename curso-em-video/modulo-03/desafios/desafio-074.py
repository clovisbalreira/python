from random import randint
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
valores = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram: ',end='')
for valor in valores:
    print(f'{valor}', end=' ')
print(f'\nO maior valor sorteado foi {max(valores)} ')
print(f'O menor valor sorteado foi {min(valores)} ')