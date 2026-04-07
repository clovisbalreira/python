from abc import ABC, abstractmethod
import random
from rich import print

"""
    Simule o sistema de batalha entre persnagens de um RPG
    Personagem { abstract }
    + nome
    + vida
    + golpes
    + atacar(alvo, forca)
    + receber_dano(dano)
    + curar() { abstract }

    Guerreiro  
    + curar()

    Mago
    + curar()
"""
class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = [] 

    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f"[green]{self.nome}[/green]( [yellow]{self.vida}[/yellow] ) atacou [red]{alvo.nome}[/red]( [yellow]{alvo.vida}[/yellow] ) com um [blue]{golpe}[/blue] de força [yellow]{forca}[/yellow]")
            alvo.receber_dano(forca)

        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer.")    

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/blue] recebeu [red]dano de {fator} [/red]!")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "pulo giratorio", "Golpe de Machado"]
        
    def curar(self):
        fator = random.randint(0, 100)
        print(f"[blue]{self.nome}[/blue] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/green] de vida." )

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de Luz", "Magia Estatica"]

    def curar(self):
        fator = random.randint(0, 100)
        print(f"[blue]{self.nome}[/blue] fez uma magia de cura e [green]recuperou {fator} pontos[/green] de vida." )

def main():
    p1 = Guerreiro('Kratos', 2000)
    p2 = Mago('Merlin', 3000)

    p1.atacar(p2, 1000)
    p2.atacar(p1, 1000)
    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()