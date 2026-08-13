from arquivo import Arquivo

class DOC(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, 'docx', tam) 

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")