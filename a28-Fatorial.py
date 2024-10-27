from time import sleep


def fatorial(numero):
    fat = numero
    sleep(1)
    print(f"{numero} ", end="")
    numero -= 1

    while numero > 0:
        sleep(1)
        print("x ", end="")
        print(f"{numero} ", end="")
        fat *= numero
        numero -= 1

    sleep(1)
    return fat

def titulo(titulo):
    print("=" * (len(titulo) + 2))
    print(f" {titulo}")
    print("=" * (len(titulo) + 2))

def main():
    titulo("FATORIAL")

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida!")

    print(f"Calculando {numero}! = ", end="")
    print(f" = {fatorial(numero)}" if numero > 1 else "1")


main()
