import random
from time import sleep

# 0. ADVINHE O NÚMERO
# Escreva um função que faça oo computador escolher um número inteiro entre 1 e 5 e peça ao usuário tentar descobrir qual número foi escolhido pelo computador. O programa deverá escrever no terminal se o usuário acertou ou errou a adivinhação.
def adivinha():
    numero = random.randint(1, 5)
    print("Vou escolher um número entre 1 e 5. Tente adivinhar!")
    print("-=-" * 20)
    adivinha = int(input("Qual número escolhi?: "))
    print("PROCESSANDO...")
    sleep(3)
    if adivinha == numero:
        print("Que legal! Você adivinhou!")
    else:
        print(f"Xi! Não deu... Eu escolhi {numero}.")

# chama a função adivinha() para executar o jogo
# adivinha()

# 1. CARA OU COROA
# Faça uma função que a pessoa digite c para escolher cara ou k para escolher coroa. Simule o lançamento de uma moeda que resulte em cara (c) ou coroa (k) e diga se a pessoa errou ou acertou na escolha.
def jogar_moeda():
    escolha = ""
    while True:
        # Solicita ao usuário escolher "c" para cara ou "k" para coroa
        escolha = input("Escolha 'c' para cara ou 'k' para coroa: ").lower()
        # Verifica se a escolha é válida
        if escolha not in ['c', 'k']:
            print("Escolha inválida!")
        else:
            break

    # Simula o lançamento da moeda
    moeda = random.choice(['c', 'k'])

    # Compara o resultado da moeda com a escolha do usuário
    if moeda == escolha:
        print(f"Parabéns! Você acertou. A moeda resultou em {moeda.upper()}.")
    else:
        print(f"Você errou. A moeda resultou em {moeda.upper()}. Sua escolha foi {escolha.upper()}.")

# Chama a função jogar_moeda() para executar o jogo
# jogar_moeda()


# 2. JOGO DE DADOS
# Faça uma função que peça ao usuário escolher um número inteiro de 2 à 12 em seguida simule o lançamento de 2 dados simultaneamente. Compare o resultado da soma dos dois dados com a escolha do usuário e avisar se ele errou ou acertou a jogada. Exemplo: O usuário escolhe 12. Um dado resulta em 6 e o outro também.
def jogar_dados():
    escolha = 0
    while True:
        # Solicita ao usuário escolher um número inteiro de 2 a 12
        escolha = int(input("Escolha um número inteiro de 2 a 12: "))
        # Verifica se a escolha está dentro do intervalo permitido
        if escolha < 2 or escolha > 12:
            print("Número inválido!")
        else:
            break

    # Simula o lançamento de dois dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Calcula a soma dos valores dos dados
    soma_dados = dado1 + dado2

    # Compara a soma dos dados com a escolha do usuário
    if soma_dados == escolha:
        print(f"Parabéns! Você acertou. Os dados resultaram em {dado1} e {dado2}, somando {soma_dados}.")
    else:
        print(
            f"Você errou. Os dados resultaram em {dado1} e {dado2}, somando {soma_dados}. Sua escolha foi {escolha}.")

# Chama a função jogar_dados() para executar o jogo
# jogar_dados()

# 3. PAR OU ÍMPAR
# Desenvolva uma função onde o usuário joga par ou impar contra o computador. O usuário digita "par" ou digita "impar" e o programa diz quem ganhou.
def par_ou_impar():
    while True:
        # Solicita ao usuário escolher "par" ou "ímpar"
        escolha = input("Escolha 'par' ou 'ímpar': ").lower()
        # Verifica se a escolha é válida
        if escolha not in ['par', 'ímpar']:
            print("Escolha inválida!")
        else:
            break

    # Solicita ao usuário escolher um número
    numero_usuario = int(input("Escolha um número: "))

    # Gera um número aleatório para o computador
    numero_computador = random.randint(0, 5)

    # Calcula a soma dos números
    soma = numero_usuario + numero_computador

    # Determina se a soma é par ou ímpar
    resultado = "par" if soma % 2 == 0 else "ímpar"

    # Informa o resultado do jogo
    print(f"Você escolheu {escolha} e o número {numero_usuario}.")
    print(f"O computador escolheu o número {numero_computador}.")
    print(f"A soma dos números é {soma}, que é {resultado}.")

    if escolha == resultado:
        print(f"Deu {escolha}! Parabéns! Você ganhou.")
    else:
        print(f"Deu {resultado}! Você perdeu! O computador ganhou.")

# Chama a função par_ou_impar() para executar o jogo
# par_ou_impar()

'''
    S U P E R    D E S A F I O ! ! !
'''

# 4. DOIS OU UM
# Crie uma rotina que recolha o nome de 5 jogadores. O programa deverá sortear 2 ou 1 para cada um dos jogadores. Se um jogador tiver um valor diferente de todos os outros 4 ele deve ser excluído da disputa. A disputa deverá continuar até que restem apenas dois jogadores. Se na rodada nenhum jogador tiver um valor único, a rodada segue sem a retirada de nenhum jogador da disputa. A cada roda deverá ser informado o resultado da disputa e quem foi retirado, se for o caso e uma pausa no programa aguardando dar enter para continuar.

def recolher_nomes():
    jogadores = []
    for i in range(5):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        jogadores.append(nome)
    return jogadores

def sortear_valores(jogadores):
    valores = {}
    for jogador in jogadores:
        valores[jogador] = random.choice([1, 2])
    return valores

def verificar_exclusao(valores):
    contagem = {1: 0, 2: 0}
    for valor in valores.values():
        contagem[valor] += 1

    excluido = ""
    for jogador, valor in valores.items():
        if contagem[valor] == 1:
            excluido = jogador

    return excluido


def dois_ou_um():
    jogadores = recolher_nomes()

    while len(jogadores) > 2:
        valores = sortear_valores(jogadores)
        print("\nResultado da rodada:")
        for jogador, valor in valores.items():
            print(f"{valor} {jogador}")

        excluido = verificar_exclusao(valores)

        if excluido:
            print(f"\n{excluido} foi excluído(a) nesta rodada.")
            jogadores.remove(excluido)
        else:
            print("\nNenhum jogador foi excluído nesta rodada.")

        if len(jogadores) == 2:
            print("\nFINAL! Disputa de Par ou Ímpar:")
            print(f"{jogadores[0]} e {jogadores[1]}")

        print(input("\nPressione Enter para continuar..."))

    # Disputa de Par ou Ímpar
    n1 = random.randint(0, 5)
    n2 = random.randint(0, 5)
    print(f"PAR: {jogadores[0]}, lançou {n1} dedos")
    print(f"ÍMPAR: {jogadores[1]}, lançou {n2} dedos")
    soma = n1 + n2
    if soma % 2 == 0:
        print(f"\n{soma} é PAR! {jogadores[0]} ganhou a final!")
    else:
        print(f"{soma} é ÍMPAR! {jogadores[1]} ganhou a final!")

# Chama a função dois_ou_um() para iniciar a disputa
# dois_ou_um()



# EXECUÇÃO DOS EXERCÍCIOS

# 0. ADVINHE O NÚMERO
# adivinha()

# 1. CARA OU COROA
# jogar_moeda()

# 2. JOGO DE DADOS
# jogar_dados()

# 3. PAR OU ÍMPAR
# par_ou_impar()

# 4. DOIS OU UM
# dois_ou_um()