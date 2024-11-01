def cores():
    """
        Cores e estilos no termina.
        STYLE         TEXT    BACK    COR
        0 Nenhum      30      40      Branco
        1 Negrito     31      41      Vermelho
        4 Sublinhado  32      42      Verde
        7 Negativo    33      43      Amarelo
                      34      44      Azul
                      35      45      Lilás
                      36      46      Ciano
                      37      47      Cinza
        \033[STYLE;TEXT;BACKm
        \033[1;32;40m
        :return: sem retorno
    """
    cores = {
        "limpa": "\033[m",
        "t-bold": "\033[1m",
        "t-vermelho": "\033[31m",
        "t-verde": "\033[32m",
        "t-amarelo": "\033[33m",
        "t-azul": "\033[34m",
        "t-lilas": "\033[35m",
        "t-ciano": "\033[36m",
        "t-cinza": "\033[37m",
        "f-cinza": "\033[47m"
    }
    return cores

cores = cores()

def titulo(titulo):
    """
        Função que retorna um cabeçado com linhas duplas acima e abaixo do título recebido como texto no parâmetro para ser impresso no terminal antes da execução de um programa.
        :param titulo: titulo, tipo string
        :return: sem retorno
    """
    print(f"{cores['t-azul']}")
    print("=" * (len(titulo) + 2))
    print(f" {titulo.upper()}")
    print("=" * (len(titulo) + 2))
    print(f"{cores['limpa']}", end='')
