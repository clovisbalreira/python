import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione Uma Pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx", ".ods", ".cvs"],
    "pdfs": [".pdf"],
    "texto": [".doc", ".odt", ".txt"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        print(f'{pasta}')
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
