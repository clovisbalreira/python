# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por exteno, de zero até vinte.
# Seu programa deverá ler um número pelo teclado( entre 0 e 20) e mostrá-lo por extenso
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
##numero = int(input('Digite um número entre 0 a 20: '))
while True:
    numero = int(input('Digite um número entre 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[numero]}')