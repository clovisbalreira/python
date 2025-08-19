import random
import time
# Crie um programa que faça o computador jogar jokempô com você
opcoes = ('Pedra', 'Papel', 'Tesoura')
numeroAleatorio = random.randint(0, 3)
numero = int(input('Vamos jogar jokempô\nEscolha uma opção\n0 - Pedra\n1 - Papel\n2 - Tesoura\n'))
print('jo')
time.sleep(1)
print('kem')
time.sleep(1)
print('pô')
print('Você escolheu {} e o computador {}'.format(opcoes[numero], opcoes[numeroAleatorio]))
if numeroAleatorio == 0:
    if numero == 0:
        print('empate')
    elif numero == 1:
        print('Jogador vence')
    elif numero == 2:
        print('computador vence')
    else:
        print('Jogada Invalida')
elif numeroAleatorio == 1:
    if numero == 0:
        print('computador vence')
    elif numero == 1:
        print('empate')
    elif numero == 2:
        print('Jogador vence')
    else:
        print('Jogada Invalida')
elif numeroAleatorio == 2:
    if numero == 0:
        print('Jogador vence')
    elif numero == 1:
        print('computador vence')
    elif numero == 2:
        print('empate')
    else:
        print('Jogada Invalida')

