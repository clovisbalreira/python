import math
#from math import sen, cos, tan
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo 
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cossseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o cossseno de {:.2f}'.format(angulo, cossseno))
print('O ângulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))