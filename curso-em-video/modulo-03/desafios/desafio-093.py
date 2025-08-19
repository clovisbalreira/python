# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.Depois vai ler a quantidade de gols feitos em cada partida.No final, tudo isso será  guardado em um dicionario, incluindo o total de gols feitos durante o campeonato
jogador = dict()
partidas = list()
jogador['jogador'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["jogador"]} jogou? '))
for p in range(1, total + 1):
    partidas.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["jogador"]} jogou {len(jogador["gols"])} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'   => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')