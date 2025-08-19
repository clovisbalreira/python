from random import randint
# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando jogador perde, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo 
print('Vamos jogar par o ímpar')
print('-' * 30)
venceu = 0
while True:
    jogador = int(input('Diga o valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [p/i] ')).upper().split()[0]
    print(f'Você jogou {jogador} e o computador {computador}.Total de {total}', end=' ')
    print('deu par' if total % 2 == 0 else 'ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            venceu += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            venceu += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print('-' * 30)
print(f'Game Over! Você venceu {venceu} vezes')
