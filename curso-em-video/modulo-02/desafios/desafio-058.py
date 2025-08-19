from random import randint
from time import sleep
# Melhore o jogo do desafio 028 onde o computador va 'pensar' em um número entre 0 até 10, só que agora adivinhe até acertar, mostrando no final quantos palpites foram necessários para vencer
escolha = False
palpite = 0
numeroAleatorio = randint(0, 10)
while not escolha:
    numero = int(input('Tente adivinha um número de 0 a 10: '))
    print('Processando...')
    sleep(2)
    print('Você escolheu o número {}'.format(numero, numeroAleatorio))
    palpite += 1
    if numeroAleatorio == numero:
        escolha = True
    else:
        if numero < numeroAleatorio:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente novamente')
print('Parabêns você acertou!\nNo {}º Palpite.\nO número era {}'.format(palpite, numeroAleatorio))