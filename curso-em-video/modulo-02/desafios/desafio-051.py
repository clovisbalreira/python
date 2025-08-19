# Desenvolva um programa que leia o primeiro termo e a razão de uma pa . no final, mostre os 10 primeiros termos dessa progressão
primeiro = int(input('Digite o termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao + 1
for c in range(primeiro, decimo, razao):
    print('{} '.format(c), end=' ')