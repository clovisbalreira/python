def metade(n = 0, f= False):
    res = (n / 2)
    return moeda(res) if f else res

def dobro(n = 0, f= False):
    res = n * 2
    return moeda(res) if f else res

def aumentar(n = 0, t = 0, f= False):
    res = n + porcento(n, t)
    return moeda(res) if f else res

def diminuir(n = 0, t = 0, f= False):
    res = n - porcento(n, t)
    return moeda(res) if f else res

def porcento(n = 0, t = 0):
    return n * t / 100

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')

def resumo(n = 0, a = 10, d = 5):
    met =  metade(n, True)
    dob = dobro(n, True)
    aum = aumentar(n, a, True)
    dim = diminuir(n, d, True)
    mensagem('Resumo do valor')
    mostrarDados('Preço analisando:  ', moeda(n))
    mostrarDados('Dobro do preço:    ', dob)
    mostrarDados('Metade do preço:   ', met)
    mostrarDados(f'{a}% de aumento:    ', aum)
    mostrarDados(f'{d}% de redução:    ', dim)

def linha():
    print('-' * 30)

def mensagem(msg):
    linha()
    print(f'{msg}'.center(30))
    linha()

def mostrarDados(msg, v):
    print(f'{msg}{v}')