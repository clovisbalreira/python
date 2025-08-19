# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiro colocados
# B) Os u´ltimos colocados da tabela.
# C) Uma lista com os tims em ordem alfabética.
# D) Em que posição na tabela está o time da chapecoense
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('='*20)
print(f'Times do Brasileirão: {times}')
print('='*20)
print(f'Os 5 primeiros são: {times[:5]}')
print('='*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('='*20)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
print('='*20)
