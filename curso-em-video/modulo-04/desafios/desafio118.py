from rich import print
from rich.panel import Panel

"""
    Crie uma classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
"""

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
    
    # Considere
    # Consumo padrão: 400g por pessoa
    # Preço: R$ 82,40/kg
    def analisar(self):
        carne = .4
        preco = 82.40
        totalCarne = self.quantidade * carne
        precoTotal = totalCarne * preco
        precoPessoa = precoTotal / self.quantidade
        caixa = caixa = Panel(f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade}[/] convidados\nCada participante comerá {carne}Kg e cada carne Kg custa R$ {preco:,.2f}\nRecomendo [blue] comprar {totalCarne:,.3f}Kg[/] de carne\nO custo total será de [green]R$ {precoTotal:,.2f}[/]\nCada pessoa pagará [yellow]R$ {precoPessoa:,.2f}[/] para participar.", title=f"{self.titulo}", width=100)
        print(caixa)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()