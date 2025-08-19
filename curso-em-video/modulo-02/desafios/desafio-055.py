# Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}º da pessoa: (Kg) '.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))