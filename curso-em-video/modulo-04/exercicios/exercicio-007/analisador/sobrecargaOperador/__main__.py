from Carteira import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)
    print( c1 == c2)
    c1 += 50
    print(c1)
    c1 -= 50
    print(c1)
    if (c1 == c2):
        print("Vocês tem o mesmo valor na carteira.")
    else:
        print("As carteira tem  valores diferentes.")
    print(c2)

if __name__ == "__main__":
    main()