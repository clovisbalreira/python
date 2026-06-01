from Pessoa import Pessoa
from Aluno import Aluno
from rich import print, inspect

"""
Implemente a seguinte estrutura de diagrama de classe 
"""
def main():
    print("criando a conta...")
    a1 = Aluno('Maria', 2000, 'ADM')
    #a1.idade = 2
    a1.nascimento = 2010
    a1.add_curso('MODA')
    a1.curso = 'MODA'
    inspect(a1, private=True, methods=True)

if __name__ == "__main__":
    main()