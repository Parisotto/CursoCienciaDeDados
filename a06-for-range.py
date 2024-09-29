# for e range

lista = ["Brasil", "EUA", "Inglaterra", "Itália", "França", "Alemanha"]
for country in lista:
    print(country)

for caracter in "Ciência de Dados":
    print(caracter)

meninas = [["Amélia", "Ana Paula", "Alice"],["Beatriz", "Bianca", "Berenice"],["Sofia", "Sandra"]]
for menina in meninas:
    print(menina)
    for nome in menina:
        print(nome)


tupla = ("São Paulo", "Paris", "Roma", "Londres")
for capital in tupla:
    print(capital)

# set
for linguagem in {"Python", "Java", "Kotlin", "JavaScript"}:
    print(linguagem)

# dicionário
for numero in {"Pi":3.15,"Phi":1.618,"e":2.72}:
    print(numero)


# RANGE:
for i in range(5):
    print(i)

for i in range(2,9):
    print(i)

for i in range(5, 17, 2):
    print(i)

lista1 = list(range(1, 10))
print(lista1)

tabuada = int(input("Tabuado do: "))
print(f"Tabuada do {tabuada}")
for multiplicador in range(1,11):
    print(f"{tabuada} x {multiplicador} = {tabuada*multiplicador}")
    
