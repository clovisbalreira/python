from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('João', 20, 'Matemática', 'Turma A')
    inspect(a1, methods=True)
    a1.fazer_matricula('Matemática', 'Turma A')
    a1.estudar()
    p1 = Professor('Maria', 35, 'Física', 'Doutorado')
    inspect(p1, methods=True)
    p1.dar_aula()
    p1.estudar()
    f1 = Funcionario('Carlos', 30, 'Secretário', 'Administração')
    inspect(f1, methods=True)
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()