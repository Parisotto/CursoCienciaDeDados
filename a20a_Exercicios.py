import random

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

# Chama a função para executar o jogo
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

# Chama a função para executar o jogo
# jogar_dados()

# 3. PAR OU ÍMPAR
# Desenvolva uma função onde o usuário joga par ou impar contra o computador. O usuário digita "par" ou digita "impar" e o programa diz quem ganhou.
def par_ou_impar():
    while True:
        # Solicita ao usuário escolher "par" ou "ímpar"
        escolha = input("Escolha 'par' ou 'ímpar': ").lower()
        # Verifica se a escolha é válida
        if escolha not in ['par', 'ímpar']:
            print("Escolha inválida. Escolha 'par' ou 'ímpar'.")
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

# Chama a função para executar o jogo
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

def disputa():
    jogadores = recolher_nomes()

    while len(jogadores) > 2:
        valores = sortear_valores(jogadores)
        print("\nResultado da rodada:")
        for jogador, valor in valores.items():
            print(f"{jogador}: {valor}")

        excluido = verificar_exclusao(valores)

        if excluido:
            print(f"\nJogador excluído nesta rodada: {excluido}")
            jogadores.remove(excluido)
        else:
            print("\nNenhum jogador foi excluído nesta rodada.")

        input("\nPressione Enter para continuar para a próxima rodada...")
        print()

    print("\nJogadores restantes:")
    for jogador in jogadores:
        print(jogador)

# Chama a função para iniciar a disputa
disputa()