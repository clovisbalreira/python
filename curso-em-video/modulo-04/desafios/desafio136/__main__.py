from pagamento import Pagamento
from pix import Pix
from boleto import Boleto
from credito import Credito

"""Crie um simulador que gerencie a pagamentos em diferentes tipos"""

def finalizar_compra(tipo_pag:Pagamento, valor:float):
    print(tipo_pag.pagar(valor))

def main():
    finalizar_compra(Pix(), 1500)
    finalizar_compra(Boleto(), 1500)
    finalizar_compra(Credito(), 1500)
    
if __name__ == "__main__":
    main()