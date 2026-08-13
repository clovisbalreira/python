from funcionario import Funcionario

class Designer(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.08