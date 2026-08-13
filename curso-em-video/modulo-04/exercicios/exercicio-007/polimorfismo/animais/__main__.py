from Animal import *
from Cachorro import Cachorro
from Spitz import Spitz
from PitBull import PitBull
from Gato import Gato
from Pato import Pato
from Galinha import Galinha


def main():
    a = Cachorro("Bandit")
    b = Gato("Mouse")
    c = Pato("Donald")
    d = Galinha("Pintadinha")
    e = Spitz("Luluzinha")
    f = PitBull("Guerreiro")

    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()
    e.emitir_som()
    f.emitir_som()

if __name__ == "__main__":
    main()