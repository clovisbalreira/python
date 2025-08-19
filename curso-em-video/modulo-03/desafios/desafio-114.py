import urllib
import urllib.request
# Crie um código em python que teste se o site Pudim está acessivel pelo computador usado.
try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('O site google não está acessível no momento.')
else:
    print('Consequi acessar o site google com sucesso.')
    print(site.read())
