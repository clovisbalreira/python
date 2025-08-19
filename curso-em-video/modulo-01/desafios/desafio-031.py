# Desenvolva um programa que pergunte a distância  de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas
distancia = float(input('Quantos distância é sua viagem: '))
'''if distancia < 200:
    preco = .50 * distancia
else:
    preco = .45 * distancia'''
preco = .50 * distancia if distancia < 200 else .45 * distancia
print('Sua viagem é de {:.2f}Km\nO valor será de R$ {:.2f}'.format(distancia, preco))
    