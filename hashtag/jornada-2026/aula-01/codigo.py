# Bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time

def caminhoMouse(valorX, valorY):
    pyautogui.click(x=valorX, y=valorY)

def escreverExecutar(texto, acao):
    pyautogui.write(texto)
    pyautogui.press(acao)

def escreverExecutarNulo(texto, acao):
    if texto != "nan":
        pyautogui.write(texto)
    pyautogui.press(acao)


# Configurar a configurar para demorar um segundo para configurar
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: entrar no sistema da empresa
# Abriria o navegador
# Apertar tecla
pyautogui.press("win")
# Escrever Texto
escreverExecutar("chrome", "enter")
escreverExecutar(link, "enter")

# Fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: fazer login da empresa
# Clicar no ponto de email
caminhoMouse(480, 429)
escreverExecutar("pythonimpressionador@gmail.com", "tab")
escreverExecutar("1234", "tab")
pyautogui.press("enter")

# Fazer uma pausa para carregar o site
time.sleep(4)

# Passo 3: abrir a passe de dados
# pip install pandas openpyxl
import pandas
# tabela = pandas.read_csv("produtos.csv")
tabela = pandas.read_csv(r"D:\git-hub\python\hashtag\jornada-2026\aula-01\csv\produtos.csv")

for linha in tabela.index:
    # Passo 4: cadastrar um produto
    caminhoMouse(432, 311)
    escreverExecutar(str(tabela.loc[linha, "codigo"]), "tab")
    escreverExecutar(str(tabela.loc[linha, "marca"]), "tab")
    escreverExecutar(str(tabela.loc[linha, "tipo"]), "tab")
    escreverExecutar(str(tabela.loc[linha, "categoria"]), "tab")
    escreverExecutar(str(tabela.loc[linha, "preco_unitario"]), "tab")
    escreverExecutar(str(tabela.loc[linha, "custo"]), "tab")
    escreverExecutarNulo(str(tabela.loc[linha, "obs"]), "tab")
    pyautogui.press("enter")
    # Voltar Inicio da tela
    pyautogui.scroll(5000)

# Passo 5: repetir o passo 4 até acabar
