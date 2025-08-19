# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preçoes na sequencia
# No final, mostre uma listagem de preçõs organizando os dados em forma tabular
lista = ( 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print(f'{"Listagem de preços":.^30}')
print('-' * 30)
for c in range(0 , len(lista), 2):
    print(f'{lista[c]:.<19} R$ {lista[c+1]:.>7.2f}')
print('-' * 30)