# Escreva um programa que converte uma temperatura digitada em °C e converta para °F
celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = 9 * celsius / 5 + 32
print('A temperatura de {}°C  corresponde a {}F!'.format(celsius, fahrenheit))