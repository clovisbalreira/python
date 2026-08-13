from validador import Validador
import re

class Email(Validador):
    def validar(self, valor:str) -> bool:
           regex = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$"
           if re.fullmatch(regex, valor):
               return True
           else:
               return False