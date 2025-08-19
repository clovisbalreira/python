# Crie um programa que vao ler vários n´meros e colocar em um lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores impares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas 
valores = list()
pares = list()
impares = list()
while True:
    numero = int(input('Digite um valor: '))
    valores.append(numero)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=' * 15)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de impares é {impares}.')