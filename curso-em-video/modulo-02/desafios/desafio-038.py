# Escreva um programa que leia  dois números inteiros e compare-os , mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois números são iguais
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Os números que você digitou são {} e {}'.format(n1, n2))
if n1 > n2:
    print('O primeiro número é maior')
elif n1 < n2:
    print('O segundo número é maior')
else:
    print('Os dois números são iguais')