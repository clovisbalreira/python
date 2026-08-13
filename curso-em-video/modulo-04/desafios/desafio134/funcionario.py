from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario

    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float = None):
        if valor is None:
            raise ValueError("Impossivel reajustar o salário desse jeito!")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Você não pode reduzir um salário de um funcionário.")

    def __str__(self):
        return f"{self.nome} ganha R$ {self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R$ {self.calcular_bonus()}"