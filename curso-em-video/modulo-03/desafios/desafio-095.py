# A primore o desafio 093 pra que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento  de cada jogador jogador = dict()
jogadores = list()
partidas = list()
jogador = dict()
while True:
    partidas.clear()
    jogador.clear()
    jogador['Jogador'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
    for p in range(1, total + 1):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
    print('-' * 20)
print('-=' * 40)
print(jogadores)
print('-=' * 40)

print(f'{"cod "}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    escolha = int(input('Mostrar dados de qula jogador? (999  interrompe) '))
    if escolha == 999:
        break
    if escolha <= len(jogadores) - 1:
        print(f'-- Levantamento do jogador {jogadores[escolha]["Jogador"]}:')
        for k, v in enumerate(jogadores[escolha]["Gols"]):
            print(f'     No {k + 1} fez {v} gols.')
        print('-' * 40)
    else:
        print(f'Erro não existe o jogador com o codigo {escolha}! Tente novamente.')
print('Volte sempre')
