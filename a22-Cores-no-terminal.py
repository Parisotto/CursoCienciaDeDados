# Cores e estilos no terminal.
# STYLE         TEXT    BACK    COR
# 0 Nenhum      30      40      Branco
# 1 Negrito     31      41      Vermelho
# 4 Sublinhado  32      42      Verde
# 7 Negativo    33      43      Amarelo
#               34      44      Azul
#               35      45      Lilás
#               36      46      Ciano
#               37      47      Cinza
# \033[STYLE;TEXT;BACKm
# \033[1;32;40m
print("\033[1;32;40mEste é o texto!")
print("\033[31mOlá, Mundo!")
print("\033[0;31mOlá, Mundo!")
print("\033[4;33;40mBrasil")
print("\033[1;31;43mPython")
print("\033[0mPython")
print("\033[1;30;45mPython\033[m")
print("\033[1;0;45m PyCharm \033[1;31;44m Python")

azul = "\033[1;34m"
limpa = "\033[m"
nome = "Parisotto"
print(f"{limpa}")
print(f"Olá, {azul}{nome}{limpa}! Como vai?")

cores = {
    "limpa":"\033[m",
    "azul":"\033[34m",
    "amarelo":"\033[33m",
    "verde":"\033[32m",
    "lilas":"\033[35m",
    "vermelho":"\033[31m",
    "bold":"\033[1m"
}

print(f"{cores['azul']}Curso {cores['verde']}Ciência {cores['amarelo']}de {cores['bold']}{cores['lilas']}Dados {cores['limpa']}com Python!")