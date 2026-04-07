from rich import print
"""
    Crie a classe caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa
"""
class Caneta:
    def __init__(self, cor = 'azul'):
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampada = True
        
    def escrever(self, msn):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!", end=' ')
        else:
            print(f"{self.cor}{msn}[/]", end=' ')

    def destampar(self):
        self.tampada = False
    
    def tampar(self):
        self.tampada = True

    def quebrar_linha(self):
        print('\n')

c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')


c1.escrever("Olá, tudo bem!")
c1.quebrar_linha()
c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem!")
c1.quebrar_linha()
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")

c1.quebrar_linha()
c1.tampar()
c1.escrever("Olá, tudo bem!")
c1.quebrar_linha()