from rich import print
from rich.panel import Panel
"""
    Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples ( canal, volume e liga/desliga)
"""
class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 5
    def __init__(self, canal = 1, volume = 1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def ligar_desligar(self):
        self.ligado = not self.ligado
            
    def canal_mais(self):
        if self.ligado:
            if(self.canal_atual == ControleRemoto.canal_max):
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    
    def canal_menos(self):
        if self.ligado:
            if(self.canal_atual == ControleRemoto.canal_min):
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1
    
    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostra_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f":prohibited: A TV está desligada" 
        else:
            conteudo = f"CANAL = "
            for canal in range(self.canal_min, self.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/] "
                else:
                    conteudo += f"{canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(self.volume_min, self.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"
           

        tv = Panel(conteudo, title="TV", width=40)
        print(tv)
c1 = ControleRemoto()
while True:
    c1.mostra_tv()
    comando = str(input(f"Ligar/Desligar @    < CH{c1.canal_atual} >  - VOL{c1.volume_atual} + "))
    match comando:
        case '0':
            break
        case '@':
            c1.ligar_desligar()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()  
        case '-':
            c1.diminuir_volume()  
        case '+':
            c1.aumentar_volume()
    