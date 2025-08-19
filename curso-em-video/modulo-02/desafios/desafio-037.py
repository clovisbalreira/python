# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal
numero =  int(input('Digite uma número: '))
escolha = int(input('Escolha uma das bases para  conversão\n1 - binario\n2 - octal\n3 - hexadecimal\n'))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha não valida!!')