# Crie um programa que leia uma frase  qualquer e diga se ela é um palindromo, desconsiderando os espaços
# ex: apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
inverso = junto[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('Temos palindromo')
else:
    print('Essa frase não é um palindromo')