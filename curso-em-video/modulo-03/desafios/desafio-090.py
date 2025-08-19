# Faça um programa que leia nome e média de um aluno, guardando rambémm a situação em um dicionario. No final mostre o conteúdo da estrutura  na tela
aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovada'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovada'
for k, v in aluno.items():
    print(f'{k} é igual {v}')
