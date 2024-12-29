import os

def renomear_arquivos(folder_path):
    # Navegue até a pasta
    os.chdir(folder_path)
    
    # Passo 1: Renomear arquivos com nomes longos para nomes temporários
    temp_names = []
    for idx, filename in enumerate(os.listdir()):
        if len(filename) > 50:  # Ajuste conforme necessário para o limite do nome
            temp_name = f'temp_{idx}'
            os.rename(filename, temp_name)
            temp_names.append((temp_name, filename))
        else:
            temp_names.append((filename, filename))
    
    # Passo 2: Renomear arquivos para o formato desejado
    for temp_name, original_name in temp_names:
        new_name = original_name.replace(' ', '_').replace(' - ', '_').replace(' - Cursos online de tecnologia', '').lower()
        if new_name != temp_name:
            os.rename(temp_name, new_name)
            print(f'Renamed: {original_name} -> {new_name}')

# Exemplo de uso
caminho_pasta = "D:\\private-main\\alura\\ai\\ia_para_dados\\chatgpt_com_excel_começando_a_usar_o_chatgpt_como_assistente"
renomear_arquivos(caminho_pasta)

def listar_diretorios(folder_path):
    # Array para armazenar os caminhos dos diretórios e subdiretórios
    caminhos = []

    # Percorrer todos os diretórios e subdiretórios
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            # Renomear diretórios
            new_name = name.replace(' ', '_').replace(' - ', '_').lower()
            new_path = os.path.join(root, new_name)
            os.rename(dir_path, new_path)
            caminhos.append(new_path)
            print(f'Renamed: {dir_path} -> {new_path}')

    return caminhos

# Exemplo de uso
#caminho_pasta = "D:\\private-main"
#todos_caminhos = listar_diretorios(caminho_pasta)

# Imprimir os caminhos
#for caminho in todos_caminhos:
    renomear_arquivos(caminho)

