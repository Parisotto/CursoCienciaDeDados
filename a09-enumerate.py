# ENUMERATE:

for indice, caractere in enumerate("Ciência de Dados"):
    print(f"{indice}: {caractere}")

lista = ["Brasil", "EUA", "Inglaterra", "Itália", "França", "Alemanha"]

for indice, country in enumerate(lista):
    print(f"{indice} - {country}")

print()
for indice, country in enumerate(lista, start=3):
    print(f"{indice} - {country}")

print()
tupla = ("Norte", "Sul", "Leste", "Oeste")
for indice, cardenal in enumerate(tupla):
    print(f"{indice} - {cardenal}")

print()
dicionario = {"São Paulo": "Sudeste", "Bahia": "Nordeste", "Amazonas": "Norte", "Paraná": "Sul", "Goiás": "Centro-Oeste"}
for indice, (estado, regiao) in enumerate(dicionario.items(), start=1):
    print(f"{indice}: {estado} - {regiao}")

print()
conjunto = {"Norte", "Sul", "Norte", "Leste", "Oeste"}
for indice, valor in enumerate(conjunto):
    print(f"{indice} - {valor}")

