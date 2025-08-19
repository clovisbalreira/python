# erros e exceções
try:
    print('operação')
except Exception as erro:
    print('falha')
else:
    print('Deu certo')
finally:
    ('Sempre acontece')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a + b
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não foi possivel dividir um número por zero')
except KeyboardInterrupt:
    print('O u´sua preferiu não informar os dados')
else:
    print(f'Resultado é {r:.2f}')
finally:
    print(f'Volte sempre')