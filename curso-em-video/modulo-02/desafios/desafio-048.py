# faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e que se encontram no intervalo de 1 ate 500.
acumulador = 0
soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        acumulador += 1
        soma += c
print('A soma dos {} acumuladores é {}'.format(acumulador, soma))

acumulador = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        acumulador += 1
        soma += c
print('A soma dos {} acumuladores é {}'.format(acumulador, soma))