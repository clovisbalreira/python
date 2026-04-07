from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

"""
    Crie a estrutra capaz de calcular salários de funcionários diferentes
    Funcionario { abstract }
    + nome
    + sal_bruto
    + salario
    + sal_min = 1612
    + inss = 7.5
    + calc_sal() { abstract }
    + analisar_sal()

    Horista
    + valor_hora
    + horas_trab
    + calc_sal()

    Mensalista
    + calc_sal()

"""
class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass
    
    def analisar_salario(self): 
        base = self.salario / self.sal_min
        conteudo = f"O salário de [blue]{self.nome}[/blue] ( [purple]{type(self).__name__}[/purple] ) é de [green]R$ {self.salario:.2f}[/green] e corresponde a [yellow]{base:.1f} salários minímos[/yellow]."
        caixa = Panel(conteudo, title= "Análise de Salário", width=35)
        print(caixa)

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab
        
    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)

def main():
    f1 = FuncionarioHorista('Paulo', 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioMensalista('Amanda', 9500)
    f2.calcular_salario()
    f2.analisar_salario()

if __name__ == "__main__":
    main()
