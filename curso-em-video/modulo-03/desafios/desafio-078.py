# Faça um programa que leia 5 valores numéricos e gaurde-os em uma lista 
# no final, mostre qual foi o mair e o menor valor digitado e sua respectivas posições na lista
valores = []
maior = menor = 0
print('=-' * 15)
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-' * 15)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end=' ')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end=' ')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}...', end=' ')