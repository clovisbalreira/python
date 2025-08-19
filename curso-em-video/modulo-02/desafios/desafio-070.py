# Crie um programa que leia o nome e o preço de vários produtos.O programa deverá pergunta se o usuário vai continuar.No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato
total = caro = precoBarato = 0
nomeBarato = ''
print('Loja Super Baratão')
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    opcao = ' '
    total += preco
    if preco > 1000:
        caro += 1
    if precoBarato == 0 or precoBarato > preco:
        nomeBarato = produto
        precoBarato = preco
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if opcao == 'N':
        break
print('Fim do programa')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomeBarato} que custa R$ {precoBarato:.2f}')
