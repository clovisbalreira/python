from validador import Validador
import re

class Usuario(Validador):
    def validar(self, valor:str) -> bool:
        regex = r"^[a-z0-9_]{5,20}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False

