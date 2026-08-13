from Pessoa import Pessoa
from Aluno import Aluno
from rich import print, inspect

"""
Implemente a seguinte estrutura de diagrama de classe 
"""
def main():
    print("criando a conta...")
    p = Aluno('Clóvis', 1980, 'ADM')
    #p.idade = 2
    #p.nascimento = 2010
    p.add_curso('MODA')
    p.curso = 'MODA'
    inspect(p, private=True, methods=True)

if __name__ == "__main__":
    main()