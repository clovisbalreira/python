from rich import print
"""
    Crie uma classe funcionario, onde podemos cadastrar nome, setor e cargo. 
    Crie tambem um metodo que permita ao funcionario se apresentar.
"""
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = 'Curso em video'

    def apresentacao(self):
        print(f":writing_hand:  Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}.")
    
c1 = Funcionario("Maria", "Administração", "Diretora")
c1.apresentacao()

c2 = Funcionario("Pedro", "TI", "Programador")
c2.apresentacao()

    
