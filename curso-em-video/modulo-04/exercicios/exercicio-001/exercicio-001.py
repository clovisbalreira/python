#Declarando classe
class Gafanhoto:
    def __init__(self):
        #Atributos da instância
        self.nome = ""
        self.idade = 0
    #Metodos da instância
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
        
#Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Clóvis"
g1.idade = 45
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 73
print(g2.mensagem())
g2.aniversario()
print(g2.mensagem())
