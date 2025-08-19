# Aprimore o sistema anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados 
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha
matriz = [[],[],[]]
pares = coluna = linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 20)
for posL, l in enumerate(matriz):
    for posC, c in enumerate(l):
        if c % 2 == 0:
            pares += c
        if posC == 2:
            coluna += c
        if posL == 1 and linha < c:
            linha = c
        print(f'[{c:^5}]', end=' ')
    print()
print('-=' * 20)
print(f'A soma dos valore pares é {pares}')
print(f'A soma dos valore da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {linha}')
