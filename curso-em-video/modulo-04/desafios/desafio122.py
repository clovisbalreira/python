from rich import print
from rich.panel import Panel
"""
    Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples ( canal, volume e liga/desliga)
"""
class ControleRemoto:
    def __init__(self):
        self.funcionamento = False
        self.numeroCanal = 1
        self.numeroVolume = 1
        self.statusTv()

    def statusTv(self):
        if(self.funcionamento):            
            tv = Panel(f"\n{self.canal()}\n\n{self.volume()}", title=f"[ TV ]", width=50)
        else:
            tv = Panel(f":stop_sign: [red]A TV está desligada[/]", title=f"[ TV ]", width=50)
        print(tv)
        botaoControle = str(input(f"@ LIGAR/DESLIGAR  < CH{self.numeroCanal} >   - VOL{self.numeroVolume} + "))
        self.botaoAcionado(botaoControle)

    def botaoAcionado(self, comando):
        if comando == '@':
            if self.funcionamento:
                self.funcionamento = False
            else:
                self.funcionamento = True
        if comando == '>':
            self.numeroCanal += 1
            if self.numeroCanal == 6:
                self.numeroCanal = 1
        if comando == '<':
            self.numeroCanal -= 1     
            if self.numeroCanal == 0:
                self.numeroCanal = 5
        if comando == '-':
            if self.numeroVolume != 1:
                self.numeroVolume -= 1
        if comando == '+':
            if self.numeroVolume != 5:
                self.numeroVolume += 1
        self.statusTv()

    def canal(self):
        texto = 'CANAL: '
        for i in range(1, 6):
            if i == self.numeroCanal:
                texto += f"[bold black on yellow] {i} [/]"
            else:
                texto += f" {i} "
        return texto
    
    def volume(self):
        """
            Volume fundo cinza e valor volume verde so espaços
        """
        texto = 'VOLUME: '
        for i in range(1, 6):
            if i <= self.numeroVolume:
                texto += f"[bold green on green] [/]"
            else:
                texto += f"[bold red on red] [/]"
        return texto
tv = ControleRemoto()