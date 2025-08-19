# Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar um nova pessoa e listar todas as pessoa cadastradas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from time import sleep
from modulos.lib.interface import *
from modulos.lib.arquivos import *
from modulos.lib.numeros import *

#arq = 'cursoemvideo.txt'
pasta_dados = os.path.join(os.path.dirname(__file__), "../../modulos/lib/dados")
if not os.path.exists(pasta_dados):
    os.makedirs(pasta_dados)
arq = os.path.join(pasta_dados, 'cursoemvideo.txt')

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerAquivo(arq)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        cabeçalho('Erro! Digite uma opção válida!')
    sleep(2)