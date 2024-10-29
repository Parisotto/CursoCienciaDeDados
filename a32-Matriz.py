from random import choice

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
#print(matriz)

def montaMatriz(linhas, colunas):
    matriz = []
    col = []
    while linhas > len(matriz):
        while colunas > len(col):
            col.append(choice([0, 1]))

        matriz.append(col[:])
        col.clear()

    tipo = 'quadrada' if linhas == colunas else 'retangular'
    print(f"matriz {tipo} = [")

    l = c = 0
    while l < linhas:
        print(end="    [")
        while c < colunas:
            print(matriz[l][c], end=", ")
            c += 1

        print(f"\b\b]")
        c = 0
        l += 1

    print("]")

def titulo(titulo):
    print()
    print("=" * (len(titulo) + 2))
    print(f" {titulo.upper()}")
    print("=" * (len(titulo) + 2))

def main():
    titulo("Matrizes")
    linhas = int(input("Linhas: "))
    colunas = int(input("Colunas: "))

    montaMatriz(linhas, colunas)

main()