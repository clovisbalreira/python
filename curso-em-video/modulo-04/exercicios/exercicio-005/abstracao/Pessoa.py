from abc import ABC, abstractmethod
from rich import inspect

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self, curso, turma):
        print(f'{self.nome} matriculado no curso {curso} turma {turma}')
    
    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')
        

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} dando aula de {self.especialidade} no nivel {self.nivel}')
    
    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no {self.nivel}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} batendo ponto no setor {self.setor} como {self.cargo}')
    
    def estudar(self):
       print(f'{self.nome} se especializa para a área de {self.setor}')


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