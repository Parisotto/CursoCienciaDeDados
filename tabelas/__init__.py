from time import sleep
import util as ut
import json
import os

def cria_menu(menu):
    print()
    print("MENU:")
    for valor in menu:
        print(f"{valor}")

def ver_opc(opc):
    try:
        if opc == 1:
            exit()
        elif opc == 2:
            return True
        else:
            return False
    except Exception as e:
        exit()


def arquivo(nome, linhas='', add=False):
    tipo = 'w' if linhas else 'r'
    try:
        if add and linhas and os.path.exists(nome):
            dados = ""
            with open(nome, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)

            with open(nome, 'w', encoding='utf-8') as arquivo:
                dados.extend(linhas)
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        elif linhas:
            with open(nome, 'w', encoding='utf-8') as arquivo:
                json.dump(linhas, arquivo, ensure_ascii=False, indent=4)

        with open(nome, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

def registros():
    tabela = []
    times = {}
    i = 0
    while True:
        times.clear()
        i += 1
        print(f" " * 6, end='')
        print(f"Cadastrar Time {i}")
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
        print()

        tabela.append(times.copy())
    return tabela


def brasileirao(tabela):
    print(f"{ut.cores['t-azul']}")
    print("=" * 43)
    print(" " * 14, end="")
    print("BRASILEIRÃO 2024")
    print("=" * 43, end='')
    print(f"{ut.cores['limpa']}")

    print(f"{'POSIÇÃO'}{'P':>3} {'J':>3} {'V':>3} "
          f"{'E':>3} {'D':>3} {'GP':>3} {'GC':>3} "
          f"{'SG':>3} {'%':>3} ")
    print("-" * 43)

    # cores
    cinza = ut.cores['f-cinza']
    bold = ut.cores['t-bold']
    limpa = ut.cores['limpa']
    verde = ut.cores['t-verde']
    vermelho = ut.cores['t-vermelho']

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
        print(f"{indice + 1:2} {time} {cinza}{bold}"
              f"{pontos:3} {limpa}{jogos:3} "
              f"{cinza}{v:3} {limpa}{e:3} "
              f"{cinza}{d:3} {limpa}{gp:3} "
              f"{cinza}{gc:3} {limpa}{saldo:3} "
              f"{cinza}{aproveitamento:3} {limpa}")

    print("-" * 43)

    sleep(1)
    if len(melhor_ataque) > 0:
        print(f"\n{vermelho}MELHOR ATAQUE:{limpa}")
        sleep(1)
        if len(melhor_ataque) == 1:
            print(f"O {bold}{verde}{melhor_ataque[0]}{limpa} "
                  f"tem o melhor ataque do campeonato"
                  f"\ncom {bold}{verde}{ataque}{limpa} gols marcados.")
        elif len(melhor_ataque) > 1:
            print(f"O", end=" ")
            for time in melhor_ataque:
                print(f"{bold}{verde}{time}{limpa}", end=" e o ")
            print(f"\b"*5, end=" ")
            print(f"tem o melhor ataque\ndo campeonato com "
                  f"{bold}{verde}{ataque}{limpa} gols marcados cada um.")

    sleep(1)
    if len(melhor_defesa) > 0:
        print(f"\n{vermelho}MELHOR DEFESA:{limpa}")
        sleep(1)
        if len(melhor_defesa) == 1:
            print(f"O {bold}{verde}{melhor_defesa[0]}{limpa} "
                  f"tem a melhor defesa do campeonato"
                  f"\ncom {bold}{verde}{defesa}{limpa} gols sofridos.")
        elif len(melhor_defesa) > 1:
            print(f"O", end=" ")
            for time in melhor_defesa:
                print(f"{bold}{verde}{time}{limpa}", end=" e o ")
            print(f"\b"*5, end=" ")
            print(f"tem a melhor defesa\ndo campeonato com "
                  f"{bold}{verde}{defesa}{limpa} gols sofridos cada um.")
