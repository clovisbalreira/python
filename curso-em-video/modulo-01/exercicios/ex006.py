# Manipulação de texto
frase = 'Curso em Video Python'
print(frase)
# fatiamento
print(frase[9]) # v
print(frase[9:13]) # vide
print(frase[9:21]) # video python
print(frase[9:21:2]) # vdopto
print(frase[:5]) # Curso
print(frase[15:]) # python
print(frase[9::3]) # veph

# Análise
print(len(frase)) # 21
print(frase.count('o')) # 3
print(frase.count('o', 0, 13)) # 1
print(frase.find('deo')) # 11
print(frase.find('android')) # -1
print('Curso' in frase) # True

# Trasnformação
print(frase.replace('Python', 'Android')) # Curso em Video Android
print(frase.upper()) # CURSO EM VIDEO PYTHON
print(frase.lower()) # curso em video python
print(frase.capitalize()) # Curso em video python
print(frase.title()) # Curso Em Video Python
frase = '   Aprenda Python   '
print(frase.strip()) # 'Aprenda Python'
print(frase.rstrip()) # '   Aprenda Python'
print(frase.lstrip()) # 'Aprenda Python   '

# Divisão
frase = 'Curso em Video Python'
print(frase.split()) # ['Curso', 'em', 'Video', 'Python']
print('-'.join(frase)) # C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n

print("""Lorem ipsum dolor sit amet consectetur 
    adipisicing elit. Eius culpa minima 
    asperiores atque harum soluta, nemo, nobis 
    hic incidunt officia at neque iusto odio 
    repudiandae architecto doloremque numquam 
    perspiciatis magni.""")
