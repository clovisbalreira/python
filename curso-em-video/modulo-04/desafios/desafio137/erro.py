from rich import print
from rich.panel import Panel
from mensagem import Mensagem

class Erro(Mensagem):
    def __init__(self, msg:str = ""):
        super().__init__(msg, "erro", ":prohibited:")

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#ffff00 on #880000", width=50)
        print(msg)