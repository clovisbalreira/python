from random import randint
from time import sleep
# Faça um progra que tenha uma lista chamada números e duas funções sorteio() e somaPar(). A primeira função vai sortear 5 n´meros e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valore pares sorte ados pela função anterior
def sorteio(lista):
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteio(numeros)
somaPar(numeros)
