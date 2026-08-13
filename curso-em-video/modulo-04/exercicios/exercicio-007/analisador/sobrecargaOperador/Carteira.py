class Carteira:
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você  tem R$ {self.saldo:,.2f} na carteira."

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("númeroocê não tem autorização para alterar o saldo desse jeito.")
    
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return "O saldo das contas são iguais."
        else:
            return "O saldo das contas são diferentes."

    def __iadd__(self, valor: int|float):
        self.__saldo = self.__saldo + valor
        return self

    def __isub__(self, valor: int|float):
        self.__saldo = self.__saldo - valor
        return self

"""
p1 == p2 p1.__eq__(p2)
p1 != p2 p1.__ne__(p2)
p1 <  p2 p1.__lt__(p2)
p1 <= p2 p1.__le__(p2)
p1 >  p2 p1.__gt__(p2)
p1 >= p2 p1.__ge__(p2)
p1 += p2 p1.__iadd__(p2)
p1 -= p2 p1.__isub__(p2)
"""