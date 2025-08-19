# Condição
tempo = int(input('Qunatos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')
print('Carro novo' if tempo <= 3 else 'Carro velho')

nome = str(input('Qual é seu nome? '))
if nome.upper() == 'GUSTAVO':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS')
else: 
    print('Sua média foi ruim! ESTUDE MAIS')