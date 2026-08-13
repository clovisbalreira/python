from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError(f"O pagamento só pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        #return f"R${self._valor:,.2f}"
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True, symbol=True, international=False)

    @abstractmethod
    def pagar(self, valor:float):
        pass