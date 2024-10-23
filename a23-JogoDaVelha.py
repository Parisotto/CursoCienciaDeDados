# JOGO DA VELHA em Python
# AUTOR: Edson Luiz Parisotto
# Professor de programação
# www.parisotto.net
# modificado por ... em (data)
#
import pygame
pygame.init()
pygame.mixer.music.load('mp3/game.mp3')
pygame.mixer.music.play()

casas = []
i = 1
while i <= 9:
    casas.append(" ")
    i += 1

jogada = 1
jogador = "0"

while jogada <=10:
    casa = 1

    # Monta a grade
    print("##### JOGO DA VELHA #####")
    print("=" * 25)
    for indice, valor in enumerate(casas):
        if indice != 2 and indice != 5 and indice != 8:
            print(f" {valor} |", end='')
        else:
            print(f" {valor}     {casa} | {casa+1} | {casa+2}")
            casa += 3
            if indice != 8: print("---|---|---   ---|---|---")
    print("=" * 25)

    # verifica se deu velha
    velha = []
    if jogada >= 5:
        velha.append(casas[0] != " " and casas[0] == casas[1] and casas[0] == casas[2])
        velha.append(casas[3] != " " and casas[3] == casas[4] and casas[3] == casas[5])
        velha.append(casas[6] != " " and casas[6] == casas[7] and casas[6] == casas[8])
        velha.append(casas[0] != " " and casas[0] == casas[3] and casas[0] == casas[6])
        velha.append(casas[1] != " " and casas[1] == casas[4] and casas[1] == casas[7])
        velha.append(casas[2] != " " and casas[2] == casas[5] and casas[2] == casas[8])
        velha.append(casas[0] != " " and casas[0] == casas[4] and casas[0] == casas[8])
        velha.append(casas[2] != " " and casas[2] == casas[4] and casas[2] == casas[6])

        # print(velha)
        if True in velha:
            input(f"Deu VELHA! Venceu o jogador \"{jogador}\"!")
            exit()

    # Alterna o jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

    # define a jogada
    while jogada < 10:
        casa = int(input(f"Vez do jogador \"{jogador}\"!\nEscolha uma casinha: "))
        if casa > 9 or casa < 1:
            print(f"{casa} não é uma casa válida.")
        elif casas[casa-1] != " ":
            print(f"{casa} já está ocupada.")
        else:
            break

    #grava a jogada
    if jogada < 10:
        casas[casa-1] = jogador

    if jogada < 10: print(f"\n" * 10)
    jogada += 1

print("Empate! Fim do Jogo da Velha")
