from usuario import Usuario
from aluno import Aluno
from formatoJson import FormatoJson
from formatoXml import FormatoXml

"""
    Implemente um exportados de dados funcional para json e XML
"""

def exportar_dados(formato, dados):
    print(formato.exportar(dados))

def main():
    u = [ 
            Usuario('José', 'jjsilva@hotmail.com'),
            Usuario('Ana', 'ana@gmail.com')
        ]
    a = [
            Aluno('Maria', 'Administração', '3 ano'),
            Aluno('Paulo', 'Gastronomia', '1 ano')
        ]
    exportar_dados(FormatoJson(), u)
    exportar_dados(FormatoJson(), a)
    exportar_dados(FormatoXml(), u)
    exportar_dados(FormatoXml(), a)

if __name__ == "__main__":
    main()