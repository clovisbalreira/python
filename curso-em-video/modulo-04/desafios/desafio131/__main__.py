from Retangulo import Retangulo
from rich import print, inspect

"""
  Crie um classe que representa um retangulo pelas suas medidas e area  
"""

def main():
    r = Retangulo()
    try:
      #r.base = 12
      #r.altura = 4
      r.medidas = (9,3)
    except Exception as e:
       print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")
    print(r.medidas)
    inspect(r, private=True, methods=True)
    
if __name__ == "__main__":
    main()