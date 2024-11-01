from time import sleep
import util as ut
from tabelas import arquivo as arq, cria_menu, ver_opc
from tabelas import registros
from tabelas import brasileirao as br
import os

def main():
    ut.titulo("Campeonato Brasileiro 2024")
    nomeArquivo = "tabela.txt"
    novaTabela = False

    menu = ["1 = Sair", "2 = Incluir novos"]
    if os.path.exists(nomeArquivo):
        dados = arq(nomeArquivo)
        br(dados)
        menu.append("3 = Limpar e incluir novos")

        cria_menu(menu)
        opc = input("Opção: ")
        if opc.isnumeric():
            opc = int(opc)
        else:
            exit()

        novaTabela = ver_opc(opc)

    print()
    novosDados = registros()
    tabela = arq(nomeArquivo, novosDados, novaTabela)
    br(tabela)


    sleep(1)

main()
