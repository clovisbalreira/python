import random
import time
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usúario venceu ou perdeu
numeroAleatorio = random.randint(0, 5)
numero = int(input('Tente adivinha um número de 0 a 5: '))
print('Processando...')
time.sleep(2)
print('Você escolheu o número {} e foi sorteado {}'.format(numero, numeroAleatorio))
if numeroAleatorio == numero:
    print('Parabêns você acertou!')
else:
    print('Infelizmente você errou tente novamente!')