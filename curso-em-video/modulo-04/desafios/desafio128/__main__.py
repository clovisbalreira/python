from Termostato  import Termostato
from rich import print, inspect

"""
    Implemente um termostato orientado a objeto
    minimo 16°
    maximo 30°
    começo 24°
    incremnto 0.5°
"""

def main():
    t = Termostato()
    try:
        t.temperatura = 25.4
        print(f"A temperatura é {t.ftemperatura}")
    except Exception as e:
        print(f"Houve um Problema: {e}")
    inspect( t, private=True, methods=True)

if __name__ == "__main__":
    main()