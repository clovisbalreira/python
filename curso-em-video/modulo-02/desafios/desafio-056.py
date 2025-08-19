# Desenvolva um program que leia o nome, idade e sexo de 4 pessoas. no final do programa , mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos
somaIdade = 0
maiorIdade = 0
nomeVelho = ''
mulheresNovas = 0

for c in range(1, 5):
    print('{}ª Pessoa'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite o Idade: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if maiorIdade < idade and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheresNovas += 1
print('A média de idade do grupo é {}'.format(somaIdade / 5))
print('O nome do homem mais velho é {}'.format(nomeVelho))
print('Tem {} mulheres com menos de 20 anos'.format(mulheresNovas))


