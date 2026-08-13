from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass