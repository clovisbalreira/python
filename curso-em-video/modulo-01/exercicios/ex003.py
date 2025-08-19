# Tipos primitivos
# int = 7, -4, 0, 9875
# float = 4.5, 0.076, -15.223, 7.0
# bool = True, False
# str = 'Olá', '7.5', ''

n1 = input('Digite um valor: ')
print(type(n1))
print('N1 é uma número: '.format(n1.isnumeric()))
print('N1 é uma alpha númerico: '.format(n1.isalpha()))
print('N1 não é um alpha númerico: '.format(n1.isalnum()))

n2 = int(input('Digite um valor: '))
print(type(n2))

somaN1 = int(input('Digite um valor: '))
somaN2 = int(input('Digite outro valor: '))
soma = somaN1 + somaN2
print('A soma entre {} e {} vale {}'.format(somaN1, somaN2, soma))
