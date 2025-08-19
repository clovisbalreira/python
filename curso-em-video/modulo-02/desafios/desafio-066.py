# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles(desnsiderando o flag)
soma = contagem = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    contagem += 1
print(f'A soma de {contagem} valores foi {soma}!')