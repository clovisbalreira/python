from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10