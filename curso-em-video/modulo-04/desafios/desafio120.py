from rich import print
from rich.panel import Panel
"""
    Crie a classe gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.Crie tamebém u método que permita mostrar a ficha desse gamer.
"""
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, favorito):
        self.favoritos.append(favorito)

    def ficha(self):
        jogosFavoritos = ""
        self.favoritos.sort()

        for jogo in self.favoritos:
            jogosFavoritos += f":video_game: [blue]{jogo}[/]\n"

        caixa = caixa = Panel(f"Nome real : [bold black on blue] {self.nome} [/]\nJogos favoritos:\n{jogosFavoritos}", title=f"Jogador <{self.nick}>", width=50)
        print(caixa)

j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()