from hashlib import sha256
from pwinput import pwinput

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id: int, nome: str = None, saldo: float = 0, senha: str = None):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        if senha is None:
            senha = self.pede_senha()
        self.__hash = self.__gerar_hash(senha)
        print(f"Conta {self.id} criada com sucesso. saldo atual de R${self.__saldo:,.2f}")

    def __gerar_hash(self, senha):
        return sha256(senha.encode()).hexdigest()

    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, nome:str = None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if len(nome) >= 5:
                self._titular = nome
        else:
            print('Senha não confere. Nome não alterado!')

    def __str__(self):
        #return f"A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de saldo."
        return f"Estado Atual da conta: {self.__dict__}."
    
    def validar_senha(self, chave) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:
        from pwinput import pwinput
        while True:
            senha = pwinput('Digite a senha da conta: ')
            if len(senha) >= 6:
                break
        return senha
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor: float, chave: str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: saldo INSUFICIENTE")
            else:
                print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
                self.__saldo -= valor
        else: 
            print('Senha não confere. Saque não autorizado!')
