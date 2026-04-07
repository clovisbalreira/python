import cv2

# Ler a imagem
img = cv2.imread('./frente-1-58.png')

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar binarização para facilitar a detecção de contornos
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Aplicar binarização para facilitar a detecção de contornos
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours):
    # Obter o retângulo delimitador do contorno
    x, y, w, h = cv2.boundingRect(contour)
    
    # Recortar a imagem usando as coordenadas do retângulo
    cropped_image = img[y:y+h, x:x+w]
    
    # Salvar a imagem recortada
    cv2.imwrite(f'imagem_{i}.png', cropped_image)

