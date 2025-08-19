# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média. 
n1 = float(input('Digite a 1º Nota: '))
n2 = float(input('Digite a 2º Nota: '))
media = (n1 + n2) / 2
print('O valor da 1º nota é {:.2f}\nO valor da 2º nota é {:.2f}\nSua média é {:.2f}'.format(n1, n2, media))