from formataDinheiro import formataDinheiro
from produto import Produto

class Carrinho():
    def __init__(self, produtos:list=None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __add__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + outro.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho.")

    def __str__(self):
        linha = "\n" + "-" * 30
        itens = "\n".join(str(p) for p in self.produtos)
        return f"{itens}{linha}\nTotal: {formataDinheiro(self.total)}{linha}" 