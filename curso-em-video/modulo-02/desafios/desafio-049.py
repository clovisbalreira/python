# Refaça o desafio 009, mostrando a tabuada de um número que o usúario escolher, só que agora utilizando um laço for
numero = int(input('Digite um número para sua tabuada: '))
print('A tabuada de {}'.format(numero))
print('=' * 12)
for c in range(1, 11):
    print('{} * {:2} = {:2}'.format(numero, c , numero * c))
print('=' * 12)