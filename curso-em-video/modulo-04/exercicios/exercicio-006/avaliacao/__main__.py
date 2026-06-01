from Avaliacao import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.set_nota(9)
    inspect(av1, private=True)    

if __name__ == "__main__":
    main()