from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} batendo ponto no setor {self.setor} como {self.cargo}')
    
    def estudar(self):
       print(f'{self.nome} se especializa para a área de {self.setor}')