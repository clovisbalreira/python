import requests
import time

# Link da rádio
url = "https://s18.maxcast.com.br:8702/live"

headers = {
    "Icy-MetaData": "1"  # Pede ao servidor para enviar metadados
}

# Faz a requisição em modo streaming
response = requests.get(url, headers=headers, stream=True)

# Pega o intervalo de metadados (icy-metaint)
meta_interval = int(response.headers.get("icy-metaint", 0))

if meta_interval == 0:
    print("O servidor não forneceu metadados.")
    exit()

stream = response.raw
def get_metadata(stream, meta_interval):
    # Lê o áudio até o próximo bloco de metadados
    stream.read(meta_interval)
    # Comprimento do metadado
    meta_length = ord(stream.read(1)) * 16
    if meta_length > 0:
        metadata = stream.read(meta_length).rstrip(b'\0')
        # Extrai StreamTitle
        meta_str = metadata.decode('utf-8', errors='ignore')
        if "StreamTitle='" in meta_str:
            start = meta_str.find("StreamTitle='") + len("StreamTitle='")
            end = meta_str.find("';", start)
            return meta_str[start:end]
    return None

print("Conectado à rádio. Aguardando metadados...")

try:
    while True:
        title = get_metadata(stream, meta_interval)
        if title:
            print("Música atual:", title)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrado pelo usuário.")
