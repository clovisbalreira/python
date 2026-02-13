from rich import print
"""
    Crie uma classe funcionario, onde podemos cadastrar nome, setor e cargo. 
    Crie tambem um metodo que permita ao funcionario se apresentar.
"""
class Funcionario:
    """ atributo de classe """
    empresa = 'Curso em video'
    def __init__(self, nome, setor, cargo):
        """ Atributo de estancia """
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake:  Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}."
    """Funcionario.empresa"""
    
c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

Funcionario.empresa = 'Hostnet'
c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())

    
