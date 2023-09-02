import PyPDF2
import os
from tkinter.filedialog import askdirectory

merger = PyPDF2.PdfMerger()

caminho = askdirectory(title="Selecione Uma Pasta")

lista_arquivos = os.listdir(caminho)

lista_arquivos.sort()
nome = lista_arquivos[0][0:lista_arquivos[0].find(" Aula")] 

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"{caminho}/{arquivo}")
merger.write(f"{caminho}/{nome}.pdf")
print('criado')