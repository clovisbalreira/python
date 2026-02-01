#Declarando classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade
    Para criar uma nova pessoa, use
    variavel = Gafanhoto("Clóvis", 45)
    """
    # Metodo Construtor
    def __init__(self, nome = 'vazio', idade = 0):
        #Atributos da instância
        self.nome = nome
        self.idade = idade

    #Metodos da instância
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    
     # Dunder Method
    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} e idade = {self.idade}"
        
#Declaração de objetos
g1 = Gafanhoto("Clóvis", 45)
print(g1)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Maria", 73)
print(g2)

g3 = Gafanhoto()
print(g3)

print(g1.__doc__) # Dunder Attribute - mostra documenteção
print(g1) # Mostra endereço do objeto na memoria
print(g1.__dict__) # Mostra em forma de dicionario
print(g1.__getstate__()) # Mostra em forma de dicionario
print(g1.__class__) # Nome da classe do objeto
