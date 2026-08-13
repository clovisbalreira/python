from rich import print
from rich.panel import Panel
from mensagem import Mensagem

class Alerta(Mensagem):
    def __init__(self, msg:str = ""):
        super().__init__(msg, "alerta", ":warning:")

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#000000 on #fffc1b", width=50)
        print(msg)