# Crie um programa que tenha a função leiaInt(), que vai funcionar  de forma  semelhante á função input() do python, só que fazendo a validação para aceitar apenas um valor
# ex: n = leiaInt('Digite um n')
def leiaInt(texto):
    while True:
        numero = str(input(texto)).strip()
        if numero.isnumeric():
            return numero
        print( '\033[0;31mErro! Digite um número inteiro válido.\033[m')

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')