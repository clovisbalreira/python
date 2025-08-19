# Escreva um programa que leia a velocidade de um carro
# Se a velocidade ultrapassar 80Km/h, mostre uma mensagem dizendo que ele  foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite 
velocidade = float(input('A velocidade do carro está '))
if velocidade > 80:
    multa = 7
    valorMulta = multa * ( velocidade - 80)
    print('Você passou o limite de 80Km/h\nSua multa é de R$ {:.2f}'.format(valorMulta))
print('Dirija com cuidado!')