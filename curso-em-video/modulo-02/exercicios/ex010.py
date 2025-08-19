# Laços de repetição
for c in range(1,6):
    print('{} - oi'.format(c))
print('Fim')

for c in range(6,0,-1):
    print('{} - oi'.format(c))
print('Fim')

for c in range(1,6,2):
    print('{} - oi'.format(c))
print('Fim')

i = int(input('Inicio '))
f = int(input('Fim '))
p = int(input('Passo '))

for c in range(i,f,p):
    print('{} - oi'.format(c))
print('Fim')

s = 0
for c in range(1,4):
    v = int(input('Digite um valor '))
    s += v
print('O total é {}'.format(s))
