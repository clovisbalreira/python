#import math
from  math import hypot
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
oposto = float(input('Comprimento cateto oposta: '))
adjacente = float(input('Comprimento cateto adjacente: '))
# hipotenusa = ( oposto ** 2 + adjacente ** 2 ) ** (1/2)
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))