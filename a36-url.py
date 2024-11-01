import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://parisotto.com.br')
except urllib.error.URLError:
    print("Erro de acesso ao site.")
else:
    print('Site acessado com sucesso!')

print(site.read())
