from arquivo import Arquivo

class PDF(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, 'pdf', tam) 

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")