# Interactive help
#help(print)
#print(input.__doc__)
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param i: passo da contagem
    :param i: sem retorno
    '''
    c =  i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
help(contador)

def soma(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
soma(8, 4)

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')
a = 2
teste(a)
print(f'A fora vale {a}')

def somaReturno(a, b, c=0):
    s = a + b + c
    return s
print(somaReturno(8, 4))

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os fatoriais são {f1} - {f2} - {f3}')