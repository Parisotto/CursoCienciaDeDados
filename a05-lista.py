# lista
# lista = [valor1, valor2, ...]
# lista = list(valor1, valor2, ...)

listaVazia = []  # cria lista vazia

listaComElementos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaComElementosMista = [7, "Pyton", 3.14159, True, 'c']
listaComRange = list(range(10))

# FATIAMENTO
listaComElementos[-1]  # pega o último elemento de uma lista
listaComElementos[:4]  # paga os 4 primeiros elementos, ou índice 3
listaComElementos[3:]  # pega o elemento do índice 3 em diante
listaComElementos[3:8]  # pega do índice 3 ao oitavo elemento, ou ínfice 7
listaComElementos[3:8:2]  # pega do índice 3 ao oitavo elemento de 2 em 2
listaComElementos[::2]  # pega todos os elementos desde o ínicio de 2 em 2

len(listaComElementos)  # retorna número de elementos
max(listaComElementos)  # retorna maior valor
min(listaComElementos)  # retorna menor valor
sum(listaComElementos)  # retorna a soma de todos os elementos
sorted(listaComElementos)  # retorna a lista ordenada

listaVazia.append(1)  # adiciona um elemento
listaVazia.append(2)  # adiciona um elemento
listaVazia.append(3)  # adiciona um elemento

listaVazia.insert(1, 9)  # insere elemento 9 no índice 1
listaVazia.remove(2)  # remove o primeiro elemento 2 da lista
listaVazia.pop()  # remove o último elemento
listaVazia.pop(0)  # remove e retorna o elemento no índice 0
listaVazia.index(3)  # retorna o índice da primeira ocorrencia do elemento
listaVazia.count(2)  # retorna o número de ocorrências do elemento
listaVazia.sort()  # Ordena crescentemente
listaVazia.sort(reverse=True)  # Ordena decrescente
listaVazia.reverse()  # Ordena os índices decrescente
listaVazia.copy()  # copia todos os elementos.

temElemento = 3 in listaComElementos  # retorna True se tiver o elemento

procurar = 7
encontrado = False

while not encontrado:
    if procurar in listaComElementos:
        encontrado = True
    else:
        procurar = int(input("Digite um número: "))

print(f"O número {procurar} foi encontrado na lista.")

# Compreensão de listas (List Comprehension)
# nova_lista = [expressão for elemento in lista_original if condição]

print()
valores = [valor for valor in listaComElementos if valor > 3]
print(valores)
soma = sum(valores)
print(soma)

print()
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)

# OU
print()
quadrados = []
for x in range(1, 6):
    quadrados.append(x**2)
print(quadrados)

print()
pares = [x for x in range(10) if x % 2 == 0]
print(pares)

print()
palavras = ["Curso", "Ciência", "de", "Dados"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)

# OU
print()
maiusculas = []
for palavra in palavras:
    maiusculas.append(palavra.upper())
print(maiusculas)

numeros = list(range(6))  # intervalo, faixa de 0 a 5
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # Saida: [2 ,4]

# Expressões Complexas
print()
pares_soma = [(x, y, x + y) for x in range(2) for y in range(2, 4) if (x + y) % 2 == 0]
print(pares_soma)

print()
pares_soma = []
for x in range(2):
    for y in range(2, 4):
        if (x + y) % 2 == 0:
            pares_soma.append((x, y, x + y))
print(pares_soma)

lista = ["Brasil", "Argentina", "Canadá", "EUA"]
lista.insert(1, "Russia")
lista.reverse()
print(lista)
