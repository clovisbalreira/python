from Credencial import Credencial
from rich import print, inspect

"""
    Crie uma classe que gerencie a hash SHA256 de um senha    
"""

def main():
    c = Credencial()
    c.senha = 'Gafanhoto'
    inspect(c, private=True, methods=True)
    print(c.validar('Gafanhoto'))
    
if __name__ == "__main__":
    main()