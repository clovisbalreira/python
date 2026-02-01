from rich import print

"""
    Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura
    reverse_button
"""

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginaAtual = 1
        print(f":book: [blue]Você acabaou de abrir o livro '[/][red]{self.titulo}[/] [blue]que tem[/] [green]{self.paginas} páginas[/][blue] no total. Você agora está na[/] [yellow]página {self.paginaAtual}[/]")

    def avancar_pagina(self, pagina):
        for i in range(self.paginaAtual + 1, self.paginaAtual + pagina + 1):
            if i < self.paginas + 1:
                print(f"Pág{i} :play_button:", end=" ")
        self.paginaAtual += pagina
        if self.paginaAtual >= self.paginas:
            self.paginaAtual = self.paginas
        print(f"[blue]Você avançou {pagina} página e agora está na [/][yellow]página {self.paginaAtual}[/]")
        if(self.paginaAtual == self.paginas):
            print(f":stop_sign: [red]Você chegou ao final do livro '{self.titulo}'[/]")
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(10)