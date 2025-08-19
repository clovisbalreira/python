# Dicionario
dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade']
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())
for k, v in dados.items():
    print(f'O {k} é {v}')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)