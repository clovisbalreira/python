# Faço um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1
print('Você digitou o número {} seu antecessor é {} e seu sucessor é {}'.format(numero, antecessor, sucessor))