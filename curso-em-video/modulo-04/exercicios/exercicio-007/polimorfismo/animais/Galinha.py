from Animal import Animal

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} Acabou de dizer 'PÓ! PÓ! PÓ!'")