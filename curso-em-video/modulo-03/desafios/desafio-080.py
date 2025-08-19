# Crie um programa que o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção 9 (sem usar o sort()). No final, mostre a lista ordenada na tela
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        if c == 0:
            print('Primeiro número adicionado')
        else:
            print('Adicionado ao final da lista...')
    else:
        for pos, n in enumerate(lista):
            if n > num:
                lista.insert(pos, num)
                print(f'Adicionado na {pos} posição da lista...')
                break
print('-=' * 15)
print(f'Os valores digitadores em ordem foram {lista}')