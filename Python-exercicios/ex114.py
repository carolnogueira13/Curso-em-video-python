# PROGRAMA O SITE ESTÁ ACESSÍVEL
import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento!")
else:
    print("Consegui acessar o site Pudim no momento!")
    print(site.read())  # Acessar o conteúdo html do site
