# Operações aritméticas
# + Adição
# - Subtração
# * Multiplicação
# / divisão
# ** Potencia
# // Divisão inteira
# % Resto da divisão

# Ordem de procedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 ** 2 = 25 ou pow(5,2) mais perte a regra de procedencia
# 5 // 2 = 2
# 5 % 2 = 1

n1 = 5
n2 = 2
nome = 'Nome'

print('Adição de {} +{} = {}'.format(n1, n2 , n1 + n2 ))
print('Subtração de {} -{} = {}'.format(n1, n2 , n1 - n2 ))
print('Multiplicação de {} *{} = {}'.format(n1, n2 , n1 * n2 ))
print('Divisão de {} / {} = {}'.format(n1, n2 , n1 / n2 ))
print('Potencia de {} ** {} = {}'.format(n1, n2 , n1 ** n2 ))
print('Potencia de {} ** {} = {}'.format(n1, n2 , pow(n1, n2) ))
print('Divisão inteira de {} // {} = {}'.format(n1, n2 , n1 // n2 ))
print('Resto da divisão de {} % {} = {}'.format(n1, n2 , n1 % n2 ))
print('Prazer em de conhecer {:20}! (  coloca 20 espaços)'.format(nome))
print('Prazer em de conhecer {:>20}! ( Alinha 20 espaços a esquerda)'.format(nome))
print('Prazer em de conhecer {:<20}! ( Alinha 20 espaços a esquerda)'.format(nome))
print('Prazer em de conhecer {:^20}! ( Alinha 20 espaços no centro)'.format(nome))
print('Prazer em de conhecer {:=^20}! ( Alinha 20 espaços no centro ao redor com "=")'.format(nome))
print('Prazer em de conhecer {:=^20}!\n ( Quebra de Linha )'.format(nome))
print('Prazer em de conhecer {:=^20}!'.format(nome) , end=' ')
print('( Sem quebra de linha )'.format(nome))


