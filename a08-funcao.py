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
