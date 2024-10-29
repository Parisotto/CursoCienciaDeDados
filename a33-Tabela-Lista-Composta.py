from time import sleep

def titulo(titulo):
    print()
    print("=" * (len(titulo) + 2))
    print(f" {titulo.upper()}")
    print("=" * (len(titulo) + 2))

def tabela(planilha):
    print()
    print("-" * 23)
    print("   Tabela das Médias")
    print("=" * 23)
    print(f"{'N°':3}{'NOME':15}{'MÉDIA':>5}")
    print("-" * 23)

    for indice, elementos in enumerate(planilha):
        sleep(1)
        print(f"{indice + 1:<3}{elementos[0]:15}{elementos[2]:5.1f}")

    print("-" * 23)

    while True:
        try:
            aluno = int(input("\nVer notas do aluno número: "))
            if aluno > len(planilha): raise ValueError

            print()
            print("-" * 35)
            print(f"         Notas do aluno: {aluno}")
            print("=" * 35)
            print(f"{'NOME':15}{'N1':>5}{'N2':>5}{'N3':>5}{'MD':>5}")
            print("-" * 35)

            i = aluno - 1
            print(f"{planilha[i][0]:15}"        # nome
                  f"{planilha[i][1][0]:5.1f}"   # nota 1
                  f"{planilha[i][1][1]:5.1f}"   # nota 2
                  f"{planilha[i][1][2]:5.1f}"   # nota 3
                  f"{planilha[i][2]:5.1f}")     # média
            print("-" * 35)

        except:
            print("Encerrando o sistema.")
            exit()

def main():
    titulo("Tabela com Lista Composta")

    planilha = list()
    while True:
        nome = input("Nome: ")
        if nome == "": nome = "Anônimo"
        while True:
            try:
                atividades = float(input("Atividades: "))
                trabalho = float(input("Trabalho: "))
                prova = float(input("Prova: "))
                break
            except:
                print("ERRO: Nota inválida!")

        media = (atividades + trabalho + prova) / 3

        planilha.append([nome, [atividades, trabalho, prova], media])

        continuar = str(input("\nContinuar? [s/n]: "))
        if continuar not in "Sn":
            break

    tabela(planilha)

main()
