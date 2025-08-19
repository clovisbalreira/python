# Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todosos dicionarios em uma lista. no final, mostre 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade do grupo.
# C) Uma Lista com todas as mulheres
# D) Uma lista com todas as pessoas co idade acima da media
pessoas = list()
dados = dict()
soma = media = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo: [M/F] ')).upper().split()[0]
        if dados['Sexo'] in 'MF':
            break
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade'] 
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 20)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram : ', end='')
for p in pessoas:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['Idade'] >= media:
        for k, p in pessoa.items():
            print(f'{k} = {p};', end=' ')
print()
print('<< Encerrado >>')