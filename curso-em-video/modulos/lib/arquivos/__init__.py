import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import interface

def criarArquivo(nome):
    try:
        #a = open(nome, 'wt+')
        #a.close()
        with open(nome, 'wt+', encoding='utf-8') as a:
            pass
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def lerAquivo(nome):
    try:
        #a = open(nome, 'rt')
        with open(nome, 'rt', encoding='utf-8') as a:
            interface.cabeçalho('Pessoas Cadastradas')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n','')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except:
        print(f'Erro ao ler o arquivo!')
    #else:
        #interface.cabeçalho('Pessoas Cadastradas')
        #print(a.readlines())
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade= 0):
    try:
        #a = open(arq, 'at')
        with open(arq, 'at', encoding='utf-8') as a:
            a.write(f'{nome};{idade}\n')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try: 
            #a.write(f'{nome};{idade}\n)
            print(f'Novo registro de {nome} adicionado.')
        except:
            print('Houve um erro na hora de escrever os dados!')
        #else:
            #print(f'Novo registro de {nome} adicionado')
            #a.close()