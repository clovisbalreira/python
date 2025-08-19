# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('O valor do produto é R$: '))
# desconto = preco * .05
desconto = preco * 5 / 100
novoValor = preco - desconto
print('Esse produto custa R$: {:.2f}\nCom desconto de 5% R$ {:.2f} O novo valor é R$: {:.2f}'.format(preco, desconto, novoValor))