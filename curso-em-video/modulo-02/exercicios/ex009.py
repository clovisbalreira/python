# Condições Alinhadas
nome = str(input('Qual é seu nome: '))
if nome.upper() == 'GUSTAVO' :
    print('Que nome Bonito')
elif nome.upper() == 'PEDRO' or nome.upper() == 'MARIA' or nome.upper() == 'PAULO':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem comum')
print('Tenho um bom dia, {}'.format(nome))