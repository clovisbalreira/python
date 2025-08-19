# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00=3.27
real = float(input('Digite o quanto tem de dinheiro: R$: '))
dolar = 3.27
compra = real / dolar
print('Com R$ {:.2f} com a cotação de US$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar, compra))
