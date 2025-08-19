#  Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno( largura e comprimento) e mostre a área do terreno
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.1f}m².')

print('Controle de terrenos')
print('-' * 40)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)