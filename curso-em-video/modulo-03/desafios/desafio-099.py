from time import sleep
# Faça um programa que tenha a função cahamada maior(), que receba varios parâmetros com valore inteiros.
# Seu prograna tem que analisar todos os valores e dizer qual deles é o maior
def maior(* numeros):
    cont = numeroMaior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for n in numeros:
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
        if numeroMaior < n:
            numeroMaior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {numeroMaior}.')
    sleep(0.5)
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

