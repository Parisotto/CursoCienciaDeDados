# while():

contador = 0
while contador <= 5:
    contador += 1

print(contador)

while True:
    contador -= 1
    if contador <= 0:
        break

print(contador)

# while aninhado
linha = 1
while linha <= 5:
    coluna = 1
    while coluna <= linha:
        print("*", end=" ")
        coluna += 1
    print()
    linha += 1
