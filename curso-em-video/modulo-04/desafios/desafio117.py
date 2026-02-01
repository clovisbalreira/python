from rich import print
from rich.panel import Panel

"""
    Crie a classe produto, onde podemos cadastrar nome e o preço. 
    Crie um metodo que mostre uma etiqueta de preço do produto
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa = caixa = Panel(f"\n{self.nome} \n-------------------------- \nR$ {self.preco}", title="Produto", width=30)
        print(caixa)

p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()
    