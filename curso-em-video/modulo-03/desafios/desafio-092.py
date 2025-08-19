from datetime import date
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se por acaso a CTPS for diferente de zero, o dicionario recebera também o ano de contratação e o salario, Calcule e acrecente, alem da idade, com quantos anos a pessoa vai se aposentar
dados = dict()
anoAtual = date.today().year
dados['Nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
dados['Idade'] =  anoAtual - anoNascimento
dados['CTPS'] = int(input('Carteira de Trabalho ( 0 não tem ): '))
if(dados['CTPS'] != 0):
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35) - anoAtual
print('-=' * 20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
