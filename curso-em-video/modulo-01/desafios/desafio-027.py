# Faça um programa que leia o nome completo de uma pessoa. mostrando em sequida o primeiro e o ultimo  nome separadamente
# ex: Ana Maraia de Souza
# primeiro = Ana
# ultimo = Souza 
nomeCompleto = str(input('Digite seu nome completo: ')).strip()
nome = nomeCompleto.split()
print('Seu primeiro nome {}'.format(nome[0]))
print('Seu último nome {}'.format(nome[len(nome) - 1]))