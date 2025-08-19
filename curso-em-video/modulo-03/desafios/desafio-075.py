# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# A) Quantoas vezes apareceu o valor 9.
# B) Em que posição foi digitado o 3
# C) Quais foram os números pares
valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram', end=' ')
for valor in valores:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')
