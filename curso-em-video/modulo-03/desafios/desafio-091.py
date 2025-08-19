from random import randint
from time import sleep
from operator import itemgetter
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem sabendo o vencedor tirou o mairo número no dado
jogador = dict()
jogadores = list()
ranking = dict()
jogo = {
    'Jogaodor 1': randint(1, 6),
    'Jogaodor 2': randint(1, 6),
    'Jogaodor 3': randint(1, 6),
    'Jogaodor 4': randint(1, 6),
}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(' == Ranking dos jogadores: ==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

