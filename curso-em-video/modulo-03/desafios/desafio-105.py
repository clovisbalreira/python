# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as sequintes informações
# - Quantidade de notas
# - A maior Nota
# - A menor nota
# - A média da turma
# - A situação ( opcional )
# adicione também as docstrings da função

def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou maisnotas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se de ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dicionario = dict()
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = sum(num) / len(num)
    if sit:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'Boa'
        elif dicionario['média'] >= 5:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Ruim'
    return dicionario
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
resp1 = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp1)
resp2 = notas(3.5, 10, 6.5, sit=True)
print(resp2)
resp3 = notas(3.5, 2, 6.5, sit=True)
print(resp3)
resp4 = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp4)
help(notas)