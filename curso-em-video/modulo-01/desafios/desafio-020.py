# import random
from random import shuffle
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
nome1 = str(input('Digite o primeiro aluno '))
nome2 = str(input('Digite o segundo aluno '))
nome3 = str(input('Digite o terceiro aluno '))
nome4 = str(input('Digite o quarto aluno '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('O aluno escolhido foi: {}'.format(lista))