# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15% 
salario = float(input('Digite o salário R$ '))
if salario > 1250:
    porcento = 10    
    valor = salario + (salario * porcento / 100)
else:
    porcento = 15
    valor = salario + (salario * porcento / 100)
print('Com reajuste de {}% o salário ficará R$ {:.2f}'.format(porcento, valor))