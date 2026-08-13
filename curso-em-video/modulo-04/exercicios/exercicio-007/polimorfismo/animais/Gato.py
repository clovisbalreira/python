from Animal import Animal

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} Acabou de dizer 'MIAU! MIAU! MIAU!'")