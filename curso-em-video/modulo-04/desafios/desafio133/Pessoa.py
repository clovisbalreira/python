from abc import ABC
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome='', nascimento=0):
        self._nome = nome
        self._nascimento = nascimento
        self.anoAtual = datetime.now().year

    @property
    def idade(self):
        return self.anoAtual - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise ValueError("Você não pode alterar a idade. Mude o ano de nascimento.")

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if ano > self.anoAtual or ano < 1990:
            raise ValueError(f"Ano {ano} é inválido")
        else:
            self._nascimento = ano