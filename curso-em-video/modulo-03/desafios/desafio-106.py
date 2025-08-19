from time import sleep
# Faça um um mini-sistema que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer.Quando   o usuário digitar a palavra 'FIM',  o programa se encerrará. obs: use cores. 
paletaCor = ['\033[m','\033[0;30;41m','\033[0;30;42m','\033[0;30;43m','\033[0;30;44m','\033[0;30;45m','\033[7;30m']
def ajuda(comando):
    titulo(f'Acessando o manual do comando \´{comando}´', 4)
    sleep(1)
    print(paletaCor[6], end='')
    help(comando)
    print(paletaCor[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(paletaCor[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(paletaCor[0], end='')
    sleep(1)
    
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)