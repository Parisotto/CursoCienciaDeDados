# função (def)

def hello(nome):
    mensagem = f"Hello, {nome}! Welcome to our class."
    return mensagem


print(hello("Edson"))


def multiplicar(x, y):
    return (x * y)


print(multiplicar(7, 9))


def saudacao(nome, cumprimento="Olá"):
    print(f'{cumprimento}, {nome}')


print(saudacao("Edson"))
print(saudacao("Parisotto", "Bom dia"))


def media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0.0


print(media([15, 20, 37]))  # 24.0
