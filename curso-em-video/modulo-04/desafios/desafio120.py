from rich import print
from rich.panel import Panel
from rich import inspect
"""
    Crie a classe gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.Crie tamebém u método que permita mostrar a ficha desse gamer.
"""
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)

    def ficha(self):
        jogosFavoritos = ""
        self.favoritos
        self.favoritos = sorted(self.favoritos, key=str.lower)

        for jogo in self.favoritos:
            jogosFavoritos += f":video_game: [blue]{jogo}[/]\n"
        
        conteudo = f"Nome real : [black on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favoritos, start=1):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
inspect(j1)
j1.ficha()