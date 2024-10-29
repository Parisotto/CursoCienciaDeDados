from time import sleep

def titulo(titulo):
    print()
    print("=" * (len(titulo) + 2))
    print(f" {titulo.upper()}")
    print("=" * (len(titulo) + 2))

def pa_pg(termo, termos, progressao, razao):
    tipo = ""
    if progressao == "pa":
        tipo = "ARITMÉTICA"
    elif progressao == "pg":
        tipo = "GEOMÉTRICA"

    titulo(f"PROGRESSÃO {tipo}")

    passos = termos
    while passos > 1:
        print(f"{termo}", end=", ")

        if progressao == "pa":
            termo += razao
        elif progressao == "pg":
            termo *= razao

        passos -= 1
        sleep(1)

    return termo


def main():
    progressao = ""
    while progressao not in ["pa", "pg"]:
        progressao = input("Digite [pa ou pg]: ").lower()

    termo = int(input("Primeiro termo: "))
    if termo == 0 and progressao == "pg": termo = 1

    razao = int(input("Razão: "))
    termos = int(input("Quantos termos: "))

    print(pa_pg(termo, termos, progressao, razao))


main()
