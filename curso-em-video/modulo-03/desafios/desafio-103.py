# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quanto gols ele marcou.
# O  programa deverá  se capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido imformado corretamente.
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() ==  '':
    ficha(gols=gols)
else:
    ficha(nome, gols)