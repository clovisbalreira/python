# Crie um programa que leia duas notas de um aluno e calcule sua média , mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0:Reprovado
# Média entra de 5.0:Recuperação
# Média 7.0 ou superior:Aprovado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Você tem a 1º nota {:.2f}\nVocê tem a 2º nota {:.2f}\nA sua média ficou {:.2f}\nO aluno está em ' .format(n1, n2, media), end='')
if media < 5:
    print('Reprovado')
elif 7 > media >= 5:
#elif media < 7:
    print('Recuperação')
else:
    print('Aprovado')