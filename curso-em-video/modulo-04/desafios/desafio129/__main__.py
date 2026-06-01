from Diario import Diario
from rich import print, inspect

"""
    Simule um diario secreto orientado a objeto
"""

def main():
    d = Diario()

    d.escrever("Primeira mensagem")
    d.escrever("Você é uma pessoa simpatica")
    d.escrever("Você gosta de Python")
    #d.senha('Cev!')
    d.ler('Cev!')
    inspect(d, private=True, methods=True)

if __name__ == "__main__":
    main()