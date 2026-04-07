from abc import ABC, abstractmethod
from rich import print
from rich.table import Table

"""
    Crie classes capazes de calcular fretes de veiculos diferentes
    Transporte { abstract }
    + distancia
    + frete
    + calc_frete() { abstract }

    Moto
    + fator = 0.50
    + calc_frete()
    livre

    Caminhao
    + fator = 1.20
    + calc_frete()
    minimo 50Km

    Drone
    + fator = 9.50
    + calc_frete()
    maximo 10Km
"""

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
        
    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f"RS {self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distanciaMinima = 50

    def calc_frete(self):
        if self.distancia < self.distanciaMinima:
            return f"Raio mínimo de {self.distanciaMinima}Km"
        else:
            self.frete = self.distancia * self.fator
            return f"RS {self.frete:.2f}"

class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)
        self.distanciaMinima = 10

    def calc_frete(self):
        if self.distanciaMinima < self.distancia:
            return f"Raio máximo de {self.distanciaMinima}Km"
        else:
            self.frete = self.distancia * self.fator
            return f"RS {self.frete:.2f}"
        
def tabela(moto, caminhao, drone, dist):
    viagem = [moto, caminhao, drone]
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    for item in viagem:
        tabela.add_row(f"{dist}Km", type(item).__name__, item.calc_frete())
    print(tabela)

def main():
    dist = 80
    moto = Moto(dist)
    print(f"Frete de {type(moto).__name__} em {dist}Km = {moto.calc_frete()}")
    caminhao = Caminhao(dist)
    print(f"Frete de {type(caminhao).__name__} em {dist}Km = {caminhao.calc_frete()}")
    drone = Drone(dist)
    print(f"Frete de {type(drone).__name__} em {dist}Km = {drone.calc_frete()}")
    tabela(moto, caminhao, drone, dist)    

if __name__ == "__main__":
    main()