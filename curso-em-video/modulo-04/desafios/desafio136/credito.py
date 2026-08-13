from pagamento import Pagamento

class Credito(Pagamento):
    def pagar(self, valor:float):
        try: 
            self.valor = valor
            return f"Pagamento CONFIRMADO DE {self.fvalor} via {self.__class__.__name__}!"
        except Exception as e:
            return f"Falha no Pagamento de {self.fvalor} via {self.__class__.__name__}"