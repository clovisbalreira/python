# Desenvolva um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo 
r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas três retas {:.2f}, {:.2f}, {:.2f}\nFormam um triângulo'.format(r1, r2 ,r3))
else:
    print('Com essas três retas {:.2f}, {:.2f}, {:.2f}\nNão formam um triângulo'.format(r1, r2 ,r3))

