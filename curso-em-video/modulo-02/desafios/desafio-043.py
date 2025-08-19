import math
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5:A baixo do peso
# entre 18.5 e 25:peso ideal
# 25 até 30:Sobrepeso
# 30 até 40:Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input('Digite a sua peso? (Kg) '))
altura = float(input('Digite a sua altura? (m) '))
#imc = peso / math.pow(altura, 2)
imc = peso / (altura ** 2)
print('Seu peso {}Kg\nSua altura {}m\nSeu IMC é {:.2f}'.format(peso, altura, imc))
if imc < 18.5 :
    print('Você está baixo do peso')
elif 18.5 <= imc < 25 :
    print('Você está com peso ideal')
elif 25 <= imc < 30 :
    print('Você está sobrepeso')
elif 30 <= imc < 40 :
    print('Você está obesidade')
else :
    print('Você está obesidade mórbida')
