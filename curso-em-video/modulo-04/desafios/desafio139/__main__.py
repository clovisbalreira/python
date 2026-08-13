from usuario import Usuario
from senha import Senha
from email import Email

"""
 Crie classes para validadores de dados, com os exemplos a seguir
    Usuario
        de 5 a 20 caracteres
        letras minusculas 
        numeros
        simbolo de sublinhado
    Senha
        pelo menos 8 caracteres
        pelo menos uma maiscula
        pelo menos um simbolo
    Email
        deve conter uma unica @
        usuario pode conter letras, numeros e alguns simbolos
        os dominios contem pontos
        o TLD encerra com ponto e pelo menos 2 letras    
"""

def validar_dados(validador: Validador, valor:str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é válido? {'SIM' if resultado else 'NÃO'}")

def main():
    validar_dados(Usuario(), "guanabara_123")
    validar_dados(Email(), "guanabara@gmail.com")
    validar_dados(Senha(), "Senh@123")

if __name__ == "__main__":
    main()