from pdf import PDF
from doc import DOC

"""Crie um simulador que gerencie a abertura de diferentes tipos de arquivos"""

def main():
    a1 = PDF('teste', 1200000)
    a2 = DOC('teste', 850000)
    a1.abrir()
    a2.abrir()

if __name__ == "__main__":
    main()