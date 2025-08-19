# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.Caso o número já existe lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em rdem crescente
valores = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
print('-=' * 15)
valores.sort()
print(f'Você digitou os valores {valores}')
    