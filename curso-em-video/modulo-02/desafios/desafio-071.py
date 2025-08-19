# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
# obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
print('Banco CEV')
valor = int(input('Que valor você quer sacar? R$ '))
cedula = 50
total = valor
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} de {cedula} R$')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('Volte sempre ao Banco CEV! Tenha um bom dia')