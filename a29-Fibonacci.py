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
    termos = input("Quantos termos?: ")
    if termos.isnumeric():
        termos = int(termos)

    print(f"{termos} termos: ", end="")
    fibonacci(termos)
    sleep(1)
    print("\nEncerrando.")
    sleep(1)

#main()
#help(titulo)

def fiboRecursivo(n, c=0):
    c += 1
    print(f"[{c}]N={n}", end=' > ')
    if n == 1:
        print(f"nA=0", end=f'>>P{c-1} >>> ')
        return 0
    elif n == 2:
        print(f"nB=1", end=f'>>P{c-1} >>> ')
        return 1
    else:
        f1 = fiboRecursivo(n-1, c)
        print(f"[{c}]f1={f1}", end=' > ')
        f2 = fiboRecursivo(n-2, c)
        print(f"[{c}]f2={f2}", end=' > ')
        return f1 + f2

print(fiboRecursivo(4))