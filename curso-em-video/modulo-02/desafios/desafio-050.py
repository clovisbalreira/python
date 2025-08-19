# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. se valor digitado for impar desconsidere-o 
soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite o número: '))
    if(numero % 2 == 0):
        cont += 1
        soma += numero
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
