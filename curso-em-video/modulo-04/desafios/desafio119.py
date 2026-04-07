from rich import print
import time

"""
    Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura
"""

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginaAtual = 1
        print(f":open_book: [blue]Você acabaou de abrir o livro '[red]{self.titulo}[/]que tem[green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.paginaAtual}[/][/blue]")

    def avancar_pagina(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.paginaAtual += 1 
                print(f"Pag{self.paginaAtual} :arrow_forward: ", end='')
                time.sleep(0.5)
                cont += 1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.paginaAtual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")
    
    def fim_do_livro(self):
        if(self.paginaAtual == self.paginas):
            return True
        else:
            return False
        #return True if self.paginaAtual == self.paginas else False

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(10)