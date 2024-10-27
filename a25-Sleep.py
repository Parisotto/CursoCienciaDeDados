import random
from time import sleep

def sorteio(nomes, contador):
    sleep(1)
    sorteado = random.choice(nomes)
    print(f"O {contador}° sorteado é", end="")
    nomes.remove(sorteado)
    sleep(1)

    i = 1
    while i <= 4:
        print(".", end="")
        i += 1
        sleep(.5)

    print("\033[32m" if contador % 2 == 0 else "\033[34m", end="")
    print(f": {sorteado}!\033[m")

def contagem_regressiva():
    i = 10
    print(f"Contagem regressiva: {i}", end="")
    sleep(1)
    print("\b\b", end="")
    while i > 0:
        i -= 1
        print(f"{i}", end="")
        sleep(1)
        print("\b", end="")

    print("Sortear!")
    print("-" * 29)

def titulo(titulo):
    print("=" * (len(titulo) + 2))
    print(f" {titulo}")
    print("=" * (len(titulo) + 2))

def main():
    titulo("SORTEIO")

    nomes = ["Edson", "Sandra", "Tales", "Sofia", "Tamires"]
    contador = 1
    passo = 1
    tamanho = len(nomes)

    contagem_regressiva()

    while passo <= tamanho:
        sorteio(nomes, contador)
        contador += 1
        passo += 1
        sleep(1)

    print("Fim dos sorteios!")

main()
