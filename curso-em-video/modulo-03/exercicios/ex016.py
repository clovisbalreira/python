# Lista Compostas
pessoas = list()
dados = ['Pedro', 25]
pessoas.append(dados)
dados = ['Maria', 19]
pessoas.append(dados)
dados = ['João', 32]
pessoas.append(dados)
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
dados = ['Pedro', 25]
pessoas.append(dados[:])
dados = ['Maria', 19]
pessoas.append(dados[:])
dados = ['João', 32]
pessoas.append(dados[:])
dados.clear()
print(pessoas)
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])
