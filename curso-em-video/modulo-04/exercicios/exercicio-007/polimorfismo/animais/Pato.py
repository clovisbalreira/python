from Animal import Animal

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} Acabou de dizer 'QUACK! QUACK! QUACK!'")