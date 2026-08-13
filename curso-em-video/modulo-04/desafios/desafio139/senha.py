from validador import Validador
import re

class Senha(Validador):
    def validar(self, valor:str) -> bool:
        regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$"
        if re.fullmatch(regex, valor):
            return True
        else:
            return False