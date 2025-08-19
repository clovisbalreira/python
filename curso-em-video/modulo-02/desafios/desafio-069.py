# Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoas cadastrada, o programa deverá perguntar se o usúario quer ou não continuar.No final, mostre:
# A) quantas pessoas tem mais de 18 ano.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 ano.
maiores = homem = mulher = 0
while True:
    print('Cadastre uma pessoa')
    idade = int(input('Idade: ')) 
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    if idade >= 18:
        maiores += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao in 'N':
        break
print('Fim do programa')
print(f'Ao todo temos com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'e temos {mulher} mulheres com menos de 20 anos')