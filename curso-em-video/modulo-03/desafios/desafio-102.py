# Crie um program que tenha uma função fatorial() que receba dois pa^rametros: o primeiro que indique o número a calcular e o outro chamado show,que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta. 
    :return: O valor do fatorial de uma número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    return f
print('-' * 20)
print(fatorial(5))
print('-' * 20)
print(fatorial(5, True))
print('-' * 20)
help(fatorial)
print('-' * 20)