# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
dias = int(input('Quantos dias alugados: '))
kilometroPercorrido = float(input('Quantos kilometros Rodados: '))
custoDiaria = 60
custoKilometroRodado = .15
valorDiarias = dias * custoDiaria
valorKilometros = kilometroPercorrido * custoKilometroRodado
valorPagar = valorDiarias + valorKilometros 
print('Você ficou com o carro {} dias\nCom o valor da diaria de R$ {:.2f}\nO valor total da diaria ficou R$ {:.2f}\nVocê percorreu {}Km\nCom o valor de kilometro rodado R$ {:.2f}\nO valor total de kilometros percorrido ficou R$ {:.2f}\nO total á pagar é R$ {:.2f}'.format(dias, custoDiaria, valorDiarias, kilometroPercorrido, valorKilometros, valorKilometros, valorPagar))