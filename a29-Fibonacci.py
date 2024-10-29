from time import sleep
from uteis.utilitarios import titulo

def fibonacci(termos):
    t1 = 0
    t2 = 1
    sleep(1)
    print("0 ", end="")
    sleep(1)
    print("1 ", end="")
    while termos - 2 > 0:
        soma = t1 + t2
        sleep(1)
        print(f"{soma} ", end="")
        t1 = t2
        t2 = soma
        termos -= 1


def main():
    titulo("SEQUÊNCIA DE FIBONACCI")
    termos = int(input("Quantos termos?: "))
    print(f"{termos} termos: ", end="")
    fibonacci(termos)
    sleep(1)
    print("\nEncerrando.")
    sleep(1)

# main()
# help(titulo)

def fiboRecursivo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fiboRecursivo(n-1) + fiboRecursivo(n-2)

print(fiboRecursivo(5))