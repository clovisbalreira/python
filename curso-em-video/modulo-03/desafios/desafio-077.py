# Crie um programa que tenha uma tupla com várias palavras( não usar acentos). depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')