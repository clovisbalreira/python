# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado 
valorCasa = float(input('Qual o valor da casa R$ ')) 
valorSalario = float(input('Qual é o valor do seu salário R$ ')) 
trintaPorcentoSalario = valorSalario * 30 / 100
quantidadeAnos = int(input('Quantos anos de financiamento '))
quantidadeMeses = quantidadeAnos * 12
valorPrestacoes = valorCasa / quantidadeMeses
print('Com o valor do salário R$ {:.2f} e seu 30% correspondente R$ {:.2f}\nO valor da casa de R$ {:.2f}\nEm {} anos com {} prestações com valor de R$ {:.2f} '.format(valorSalario, trintaPorcentoSalario, valorCasa, quantidadeAnos, quantidadeMeses, valorPrestacoes))
if trintaPorcentoSalario >= valorPrestacoes:
    print('Parabens o seu finaciamento pode ser concedido')
else:
    print('Infelizmente não poderemos liberar o financiamento')