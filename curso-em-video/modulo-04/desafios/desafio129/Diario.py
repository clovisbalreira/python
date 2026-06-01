from rich import print, inspect

class Diario:
    def __init__(self, senha = 'Cev!@'):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg)

    @property
    def senha(self):
        raise RecursionError(f"Ninguem tem permissão de ver a senha")
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha.strip()

    def ler(self, senha = None):
        if senha == self.__senha:
            print(f"[green]Diario LIBERADO![/green]")
            for segredo in self.__segredos:
                print(f"- {segredo}")
        else:
            #raise ValueError(f"Senha invalida! Você não pode ler o diario!")
            print(f"[purple]Senha invalida! Você não pode ler o diario![/]")
