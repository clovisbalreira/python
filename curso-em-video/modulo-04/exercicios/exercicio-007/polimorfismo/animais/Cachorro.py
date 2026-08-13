from Animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} Acabou de dizer 'AU! AU! AU!'")