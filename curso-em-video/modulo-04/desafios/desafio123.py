from abc import ABC, abstractmethod
import math

"""
    Implemente o seguinte diagrama de classe:

    Poligono { abstract }
    + qtd_lados
    + perimetro() { abstract }
    + area() { abstract }

    Quadrado
    + lado
    + perimetro()
    + area()

    Circulo
    + raio
    + perimetro()
    + area()
    
"""
class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2

def main():
    q = Quadrado(20)
    print("Quadrado")
    print(f"Perimetro = {q.perimetro():.1f}")
    print(f"Area = {q.area():.1f}")

    c = Circulo(12)
    print("Circulo")
    print(f"Perimetro = {c.perimetro():.1f}")
    print(f"Area = {c.area():.1f}")

if __name__ == "__main__":
    main()