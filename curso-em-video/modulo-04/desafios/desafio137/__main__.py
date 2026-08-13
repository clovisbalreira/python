from mensagem import Mensagem
from erro import Erro
from alerta import Alerta

"""Implemente um sistema de mensagens padronizaas usando orientação a objetos"""

def main():
    Mensagem("Mensagem").mostrar()
    Erro("Erro").mostrar()
    Alerta("Alerta").mostrar()

if __name__ == "__main__":
    main()