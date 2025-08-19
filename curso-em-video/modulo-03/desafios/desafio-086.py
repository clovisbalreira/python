# Crie um programa que crie um matriz de dimensão 3X3 e preencha com valores lidos peolo teclado
# NO final, mostre a matriz na tela, com a formatação correta
matriz = [[],[],[]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 20)
for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end=' ')
    print()