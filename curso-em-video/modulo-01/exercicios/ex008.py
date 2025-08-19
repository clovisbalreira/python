# Cores no terminal
# ANSI escape sequence
# \033[style;text;backm
# \033[0;33;44m

# style
# 0 - sem estilo
# 1 - bold
# 2 - underline
# 7 - negative

# text
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - violeta
# 36 - azul claro
# 37 - cinza

# back 
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - violeta
# 46 - azul claro
# 47 - cinza

teste = 'Teste'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m',
         }
print('\033[0;30;41m{}\033[m'.format(teste))
print('\033[4;33;44m{}\033[m'.format(teste))
print('\033[1;35;43m{}\033[m'.format(teste))
print('\033[30;42m{}\033[m'.format(teste))
print('\033[m{}\033[m'.format(teste))
print('\033[7;30m{}\033[m'.format(teste))
print('\033[1;31;43mOlá, Mundo!\033[m')
print('{}Olá, Mundo!\033[m{}'.format(cores['pretobranco'], cores['limpa']))
