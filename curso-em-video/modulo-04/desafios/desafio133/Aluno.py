from Pessoa import Pessoa

class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = curso

    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O curso {curso} não esta na lista de cursos oficiais.")

    def add_curso(self, curso):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            self.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"O nome do {curso} está fora do padrão para cursos!")