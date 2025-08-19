# Faça um programa  que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

texto = input('Digite algo: ')
print('{} é do tipo: {}'.format(texto, type(texto)))
print('{} só tem espaços: {}'.format(texto,  texto.isspace()))
print('{} é uma numéro: {}'.format(texto, texto.isnumeric()))
print('{} é alfabetico: {}'.format(texto, texto.isalpha()))
print('{} é alfanumérico: {}'.format(texto,  texto.isalnum()))
print('{} está em maiúsculo: {}'.format(texto,  texto.isupper()))
print('{} está em miniúsculo: {}'.format(texto,  texto.islower()))
print('{} está capitalizado: {}'.format(texto,  texto.istitle()))