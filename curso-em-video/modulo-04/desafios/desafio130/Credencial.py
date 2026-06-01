import hashlib

class Credencial:
    def __init__(self):
        self.__hash = None

    def __gerar_hash(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, nova_senha):
        if(len(nova_senha) > 0):
            self.__hash = self.__gerar_hash(nova_senha)
        else:
            raise ValueError("Senha Invalida!")

    def validar(self, chave):
        hash_chave = self.__gerar_hash(chave)

        if hash_chave == self.__hash:
            print("Senha confere!")
            return True
        else:
            print("Senha não bate!")
            return False