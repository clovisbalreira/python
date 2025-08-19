# Listas
lanche = ['Hamburger', 'Suco', '', 'Pudim', 'Pizza', ]
print(lanche)
lanche[2] = 'Pizza'
print(lanche)
lanche.append('Coke')
print(lanche)
lanche.insert(0, 'Cachorro Quente')
print(lanche)
del lanche[3]
lanche.pop(3)
lanche.remove('Cachorro Quente')
if 'Cachorro Quente' in lanche:
    lanche.remove('Cachorro Quente')
print(lanche)
lanche.sort()
print(lanche)
lanche.sort(reverse=True)
print(lanche)
print(len(lanche))
valores = (range(4,11))
print(valores)