# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.No final, mostre um boletim contendo a média de cada um e permite que o usuário possa mostrar as notas de cada aluno individualmente
alunos = []
while True:
    dados = [[], [], []]
    nome = str(input('Nome: '))
    dados[0].append(nome[:])
    for n in range(1,3):
       nota = float(input(f'Nota {n}: ')) 
       dados[1].append(nota)
    totalNotas = 0
    for c in dados[1]:
        totalNotas += c
    media = totalNotas / len(dados[1])
    dados[2].append(media)
    alunos.append(dados)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for pos, aluno in enumerate(alunos):
    print(f'{pos:<4}{aluno[0][0]:<10}{aluno[2][0]:>8.1f}')
print('-' * 30)
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999  interrompe) '))
    if escolha == 999:
        break
    if escolha <= len(alunos) - 1:
        print(f'Notas de {alunos[escolha][0][0]} são {alunos[escolha][1]}')
    else:
        print('Aluno invalido!!!')
print('Finalizando...')
print('Volte sempre')