from rich import print
from rich.panel import Panel

class Mensagem():
    def __init__(self, msg:str = "", tipo:str = "aviso", icone:str = ":speech_balloon:"):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#ffffff on #000000", width=50)
        print(msg)