def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print( '\033[0;31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print( '\033[0;31mEntrada de dados interronpido pelo usúario.\033[m')
            return 0
        else:
            return n
        
def leiaFloat(texto):
    while True:
        try:
            n = float(input(texto))
        except (ValueError, TypeError):
            print( '\033[0;31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print( '\033[0;31mEntrada de dados interronpido pelo usúario.\033[m')
            return 0
        else:
            return n