# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
preco = float(input('O valor do Salário é R$: '))
# aumento = preco * .15
aumento = preco * 15 / 100
novoValor = preco + aumento
print('Esse produto custa R$: {:.2f}\nCom aumento de 15% R$ {:.2f} O novo valor é R$: {:.2f}'.format(preco, aumento, novoValor))