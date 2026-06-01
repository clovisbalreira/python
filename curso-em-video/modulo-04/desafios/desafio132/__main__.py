from ContaBancaria import ContaBancaria
from rich import print, inspect

"""
 Aprimore o exercicio da ContaBancaria , aplicando conceitos de encapsulamento
"""
def main():
    print("criando a conta...")
    cc = ContaBancaria(123, 'Gustavo', 1000)
    print("Tentando Mudar o nome do titular da conta...")
    cc.nome = 'Clóvis'
    print("Realizando deposito")
    cc.depositar(500)
    print("Realizando Saque")
    cc.sacar(200)
    cc.nome = 'Clóvis'
    inspect(cc, private=True, methods=True)

if __name__ == "__main__":
    main()