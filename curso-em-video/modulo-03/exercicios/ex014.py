# tuplas ()
# As tuplas são imutáveis
lanche =  ('Hamburguer', 'Suco', 'Pizza', 'Quindim', 'Batata frita'
)
print(lanche)
print(lanche[2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[-1])
print(sorted(lanche))
print(len(lanche))
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
print('=' * 20)
for c in lanche:
    print(f'Eu vou comer {c}')
print('=' * 20)
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
print('=' * 20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print('=' * 20)
# lanche[1] = 'Refrigerante'
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(c.count(5))
print(c.index(8))
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)