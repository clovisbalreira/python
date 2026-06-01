import hashlib

# SHA = Segure Hash Algorithm
texto = "Coração"
cod = texto.encode('utf-8')
hash = hashlib.sha1(cod).hexdigest() # hash Ja foram quebradas
print(hash)
hash = hashlib.md5(cod).hexdigest() # hash Ja foram quebradas
print(hash)
hash = hashlib.sha256(cod).hexdigest()
print(hash)