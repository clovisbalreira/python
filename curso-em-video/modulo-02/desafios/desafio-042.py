# Refaça o desafio 035 dos triânguloss, acrescentando o recurso de mostrar que tipo de triângulo será formado
# Equilátero: todos os lados iguais
# Isóscelos: dois lados iguais
# Escaleno: todos os lados diferentes
r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com essas três retas {:.2f}, {:.2f}, {:.2f}\nFormam um triângulo '.format(r1, r2 ,r3), end='')
    if r1 == r2 == r3:
        print('equilátero')
    elif r1 != r2 != r3 != r1:
        print('escaleno')
    else:
        print('isóscelos')
else:
    print('Com essas três retas {:.2f}, {:.2f}, {:.2f}\nNão formam um triângulo'.format(r1, r2 ,r3))