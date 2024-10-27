from time import sleep

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

def titulo(titulo):
    print("=" * (len(titulo) + 2))
    print(f" {titulo}")
    print("=" * (len(titulo) + 2))

def main():
    titulo("SEQUÊNCIA DE FIBONACCI")
    termos = int(input("Quantos termos?: "))
    print(f"{termos} termos: ", end="")
    fibonacci(termos)
    sleep(1)
    print("\nEncerrando.")
    sleep(1)

main()