# Funções
valores = [6, 3, 1, 0, 2]
def mostraLinha():
    print('-' * 40)

def titulo(msg):
    mostraLinha()
    print(msg)
    mostraLinha()

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

def contador(*num):
    for valor in num:
        print(f'{valor}')
    mostraLinha()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

mostraLinha()
print('Sistema de alunos')
mostraLinha()
mostraLinha()
print('Cadastro de funcionario')
mostraLinha()
mostraLinha()
print('Erro do sistema')
mostraLinha()
print()
titulo('Sistema de alunos')
titulo('Cadastro de funcionario')
titulo('Erro do sistema')
soma(b=4, a=5)
mostraLinha()
soma(7, 2)
mostraLinha()
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print(valores)
dobra(valores)


