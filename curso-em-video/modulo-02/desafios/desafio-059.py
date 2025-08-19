# crie um programa que le dois valores e mostre um menu na tela
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# seu programa dever´realizar a operação solicitada em cada caso
opcao = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while opcao != 5:
    print('1 - somar\n2 - multiplicar\n3 - maior\n4 - novos números\n5 - sair do programa\n')
    opcao = int(input('Escolha a opção: '))
    if opcao == 1:
        print('A soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        if n1 == n2:
            print('Os dois números são iguais {}'.format(maior))
        else:
            print('O maior numero de {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os dados novamente')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida. Tente novamente')

        
