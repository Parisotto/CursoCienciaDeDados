from time import sleep

def tabuada(tabuada):
    sleep(1)
    for numero in range(1, 11):
        print(f"{numero:3} x {tabuada} = {numero * tabuada:2}")
        sleep(1)

def titulo(titulo):
    print("=" * (len(titulo) + 2))
    print(f" {titulo}")
    print("=" * (len(titulo) + 2))

def main():
    while True:
        try:
            tab = int(input("Escolha um inteiro de 1 a 9: "))
            if tab < 1 or tab > 9:
                raise ValueError
            break
        except ValueError:
            print("Entrada inválida!")

    titulo(f"TABUADA DO {tab}")
    tabuada(tab)

main()