# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas 
# C) Uma listagem com as pessoas mais leves
pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).split())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    if maior < dados[1]:
        maior = dados[1]
    if menor > dados[1]:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O Maior peso foi de {maior:.1f}Kg. Peso de', end=' ')
for n in pessoas:
    if maior == n[1]:
        print(n[0], end=' ')
print(f'\nO Menor peso foi de {menor:.1f}Kg. Peso de', end=' ')
for n in pessoas:
    if menor == n[1]:
        print(n[0], end=' ')