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

def desenpacotar(* varargs):
    print(varargs)
    print(f"Tamanho: {len(varargs)}")
    for des in varargs:
        print(f"Arg: {des}")

desenpacotar(1)
desenpacotar(1, 2 , 7)

#def dobrar(valores):
def dobrar(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] *= 2
        indice += 1

valores = [7, 2, 9, 3, 0, 1]
print(valores)
dobrar(valores)
print(valores)

def alterar(numero):
    numero = 5

numero = 0
alterar(numero)
print(numero)
