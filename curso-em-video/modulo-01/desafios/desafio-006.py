# Crie um algoritmo que leia um numéro e mostre o seu dobro, triplo e a raiz quadradra
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
# raizQuadradra = numero ** (1/2)
raizQuadradra = pow(numero, (1/2))
print('Você digitou o número {}\nSeu dobro é {}\nSeu triplo é {}\nE sua raiz quadradra é {:.2f}'.format(numero, dobro, triplo, raizQuadradra))