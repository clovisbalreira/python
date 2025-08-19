# Faça um programa que tenha uma função chamada escrever(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
# ex: escreva('Olá,Mundo!')
# saida:
# -----------
#  Olá,Mundo
# -----------

def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('Cef')
