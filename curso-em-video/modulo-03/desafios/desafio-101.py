#  Crie um programa que tenha uma função chamada votar() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional ou obrigatório nas eleições
def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    frase = f'Com {idade} anos: '
    if idade < 16:
        frase += 'não vota'
    if 16 <= idade < 18 or idade > 65:
        frase += 'voto opcional'
    else:
        frase += 'voto obrigatório'
    return frase
print('-' * 20)
anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoNascimento))