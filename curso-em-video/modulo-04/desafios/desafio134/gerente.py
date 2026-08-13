from funcionario import Funcionario

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15