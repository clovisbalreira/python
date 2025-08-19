from time import sleep
# Faça um programa que tenha um função chamada contador() que receba três parâmetros: inicio, fim e a passo e realiza a contagem
# Seu programa tem que realizar três contagens atráves da função criada
# a) de 1 ate 10, de 1 em 1
# b) de 10 ate 0, de 2 em 2
# C) uma contagem personalizada

def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')   
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)