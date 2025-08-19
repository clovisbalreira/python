from random import randint
from time import sleep
# Faça um programa que ajude um jogador da mega sena a criar palpites, O programa vai perguntar quantos  jogos serão gerados e vai sortear 6 n´meros entr 1 a 60 para cada jogo, cadastrado tudo em uma lista composta
jogos = []
dados = []
contador = total = 0
print('-=' * 20)
print('         Joga na mega Sena')
print('-=' * 20)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
while True:
    numeroSorteado = randint(1, 60)
    if numeroSorteado not in dados:
        dados.append(numeroSorteado)
        contador += 1
    if contador == 6:
        total += 1
        contador = 0
        jogos.append(dados[:])
        dados.clear()
    if( total == quantidade):
        break
print(f'Sorteando {quantidade} jogos')
for p, j in enumerate(jogos):
    print(f'Jogo {p + 1}: {j}')
    sleep(1)
print('Boa Sorte')
