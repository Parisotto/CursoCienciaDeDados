from time import sleep
from uteis.utilitarios import titulo

# print(factorial(5))

def fatorialRecursiva(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorialRecursiva(n - 1)

# print(fatorialRecrusiva(5))

def fatorial(numero):
    fat = numero
    sleep(.5)
    print(f"{numero}", end=" ")
    numero -= 1

    while numero > 0:
        sleep(.5)
        print("x", end=" ")
        sleep(.5)
        print(f"{numero}", end=" ")
        fat *= numero
        numero -= 1

    sleep(.5)
    print(f"=", end=" ")
    sleep(.5)
    return fat


def main():
    titulo("Fatorial")

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida!")

    sleep(.5)
    print(f"Calculando {numero}! =", end=" ")
    print(f"{fatorial(numero)}" if numero > 1 else "1")
    sleep(1)

main()
