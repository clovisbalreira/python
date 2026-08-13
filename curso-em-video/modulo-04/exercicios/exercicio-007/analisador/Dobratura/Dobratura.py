class Numero:
    def __init__(self, valor: int|float = 0):
        self.valor = valor

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do Número"

    def dobrar(self):
        self.valor = self.valor * 2

class Texto:
    def __init__(self, txt: str = ''):
        self.texto = txt

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do Texto"

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

class Lista:
    def __init__(self, lst:list = []):
        self.valores = lst

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro do Lista"

    def dobrar(self):
        self.valores = self.valores + self.valores

class Papel:
    def __init__(self):
        self.dobrado = False

    def __str__(self):
        return f"O papel está {'novo' if not self.dobrado else 'dobrado'}"

    def dobrar(self):
        self.dobrado = True

class Casa:
    def __str__(self):
        return f"Era uma casa muito engraçada...."
    
def tenteDobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar {objeto.__class__.__name__}")