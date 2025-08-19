# laços repetição
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma foi {}'.format(s))
print(f'A soma foi {s}')
