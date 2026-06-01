from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = curso
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        existe = False
        for cursoOficial in self.cursos_oficiais:
            if cursoOficial == curso:
                existe = True

        if existe:
            self._curso = curso
        else:
            raise ValueError(f"O curso {curso} não esta na lista de cursos oficiais.")

    def add_curso(self, curso):
        self.cursos_oficiais.append(curso)