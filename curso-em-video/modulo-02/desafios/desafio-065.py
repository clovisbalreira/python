# Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
resposta = 'S'
soma = quantidade = menor = maior = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1
    if quantidade == 1:
        menor = n
        maior = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    resposta = str(input('Quer Continuar S/N: ')).upper().strip()[0]
media = soma / quantidade
print('A média dos números digitados foi {}\nO maior número foi {}\nO menor número foi {}'.format(media, maior, menor))
     