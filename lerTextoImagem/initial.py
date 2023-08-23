# pip install opencv-python
# pip install pytesseract

import pytesseract
import cv2

# passo 1: Ler imagem
imagem = cv2.imread('festa_do_sinal.jpg')

# passo 2: pedir ao tesserart extrair o texto da imagem
#texto = pytesseract.image_to_string(imagem)
#print(texto)