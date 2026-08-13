from formataDinheiro import formataDinheiro

class Produto():
    def __init__(self, nome:str, preco:float = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} ({formataDinheiro(self.preco)})"