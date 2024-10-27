def titulo(titulo):
    print("=" * (len(titulo) + 2))
    print(f" {titulo}")
    print("=" * (len(titulo) + 2))

def menor_maior(numeros):
    # print(f"\n{numeros}")
    menor = maior = numeros[0]
    soma = 0

    for n in numeros:
        if n < menor: menor = n
        if n > maior: maior = n
        soma += n

    media = soma / len(numeros)

    return [menor, maior, media]

def main():
    chances = 5
    numeros = []

    titulo("NÚMEROS MENOR E MAIOR")

    while True:
        try:
            restam = f" (restam {chances} chances)"
            numero = int(input(f"Digite um inteiro positivo, 0 para parar{restam if chances < 5 else ''}: "))
            if numero < 0: raise ValueError
            if numero == 0: break
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida")
            chances -= 1
            if chances == 0: exit()

    retorno = menor_maior(numeros)
    print(f"O menor número é {retorno[0]} e o maior é {retorno[1]}")
    print(f"A média entre os valores {numeros} é {int(retorno[2])}.")

main()