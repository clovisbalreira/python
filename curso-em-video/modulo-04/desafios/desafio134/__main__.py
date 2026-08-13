from gerente import Gerente
from designer import Designer
from desenvovedor import Desenvolvedor

""" Crie a seguinte estrutura de classes para calcular bônus salarial"""

def main():
    funcionarios = [
        Designer("Designer", 8_000),
        Desenvolvedor("Desenvolvedor", 8_000),
        Gerente("Gerente", 8_000)
    ]
    for funcionario in funcionarios:
        print(funcionario)
if __name__ == "__main__":
    main()