import pygame
import os
import time
# Faça um programa em python que abra e reproduza um audio de um arquivo MP3

# Inicializa o pygame
pygame.init()

# Pega o caminho absoluto do arquivo MP3 na mesma pasta do script
caminho_musica = os.path.join(os.path.dirname(__file__), "../../music/alagados.mp3")

# Carrega e toca a música
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play()

print("Tocando música: alagados.mp3")

# Mantém o programa aberto enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
