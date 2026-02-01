from rich import print
"""
    Crie a classe caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa
"""
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampa = False
        if(self.cor == 'azul'):
            self.cor = 'blue'
        elif(self.cor == 'vermelho'):
            self.cor = 'red'
        elif(self.cor == 'verde'):
            self.cor = 'green'

    def destampar(self):
        self.tampa = True
    
    def tampar(self):
        self.tampa = False
        
    def escrever(self, texto):
        if self.tampa:
            print(f"[{self.cor}]{texto}[/]", end=' ')
        else:
            print(f":stop_sign: A [{self.cor}]caneta[/] está tampada!", end=' ')


    def quebrar_linha(self):
        print('\n')

c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem!")
c1.quebrar_linha()
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")