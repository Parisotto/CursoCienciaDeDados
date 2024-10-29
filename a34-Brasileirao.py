from time import sleep

def titulo(titulo):
    print()
    print("=" * (len(titulo) + 2))
    print(f" {titulo.upper()}")
    print("=" * (len(titulo) + 2))

def brasileirao(tabela):
    print()
    print("=" * 43)
    print(" " * 14, end="")
    print("BRASILEIRÃO 2024")
    print("=" * 43)
    print(f"{'POSIÇÃO'}{'P':>3} {'J':>3} {'V':>3} "
          f"{'E':>3} {'D':>3} {'GP':>3} {'GC':>3} "
          f"{'SG':>3} {'%':>3} ")
    print("-" * 43)

    ataque = 0
    melhor_ataque = []
    defesa = 0
    melhor_defesa = []
    for indice, times in enumerate(tabela):
        time = str(times['time'])[:3].upper()
        v = times['vitorias']
        e = times['empates']
        d = times['derrotas']
        gp = times['gols_marcados']
        gc = times['gols_sofridos']

        pontos = v * 3 + e * 1
        jogos = v + e + d
        saldo = gp - gc
        if jogos == 0:
            aproveitamento = 0
        else:
            aproveitamento = int(pontos / (jogos * 3) * 100)

        if gp >= ataque:
            if gp != ataque:
                melhor_ataque.clear()
                ataque = gp
            melhor_ataque.append(times['time'])

        if gc <= defesa or defesa == 0:
            if gc != defesa:
                defesa = gc
                melhor_defesa.clear()
            melhor_defesa.append(times['time'])

        sleep(1)
        print(f"{indice + 1:2} {time} {pontos:3} {jogos:3} "
              f"{v:3} {e:3} {d:3} {gp:3} {gc:3} {saldo:3} "
              f"{aproveitamento:3} ")

    print("-" * 43)

    sleep(1)
    if len(melhor_ataque) == 1:
        print(f"\nMELHOR ATAQUE:")
        print(f"O {melhor_ataque[0]} tem o melhor "
              f"ataque do campeonato\ncom {ataque} gols marcados.")
    elif len(melhor_ataque) > 1:
        print(f"\nMELHOR ATAQUE:")
        print(f"O", end=" ")
        for time in melhor_ataque:
            print(time, end=", o ")
        print(f"\b"*4, end=" ")
        print(f"tem o melhor ataque\ndo campeonato com {ataque} "
              f"gols marcados cada um.")

    if len(melhor_defesa) == 1:
        print(f"\nMELHOR DEFESA:")
        print(f"O {melhor_defesa[0]} tem a melhor "
              f"defesa do campeonato\ncom {defesa} gols sofridos.")
    elif len(melhor_defesa) > 1:
        print(f"\nMELHOR DEFESA:")
        print(f"O", end=" ")
        for time in melhor_defesa:
            print(time, end=", o ")
        print(f"\b"*4, end=" ")
        print(f"tem a melhor defesa\ndo campeonato com {defesa} "
              f"gols sofridos cada um.")

def main():
    titulo("Campeonato Brasileiro 2024")

    tabela = []
    times = {}

    i = 0
    while True:
        times.clear()
        i += 1
        print(f"\n      Cadastrar Time {i}")
        print("-" * 28)
        time = input("Time: ").title().strip()
        if time == "": break
        times['time'] = time

        while True:
            jogos = int(input("Jogos: "))
            vitorias = int(input("Vitórias: "))
            empates = int(input("Empates: "))
            derrotas = int(input("Derrotas: "))

            total = vitorias + empates + derrotas
            if total != jogos:
                print(f"A soma de vitorias, empates e derrotas ({total}) "
                      f"é diferente do total de jogos ({jogos})")
                continue

            times['vitorias'] = vitorias
            times['empates'] = empates
            times['derrotas'] = derrotas
            break

        times['gols_marcados'] = int(input("Gols marcados: "))
        times['gols_sofridos'] = int(input("Gols sofridos: "))

        tabela.append(times.copy())

    brasileirao(tabela)

main()
