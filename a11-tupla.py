# Tupla
# tupla = (elemento1, elemento2, ...)

tupla = (1, "Olá", 3.14, True, 'c') # uma tupla é imutável

tupla_direta = 0, "Edson", 1.618, 'p', "Edson"
tupla_vazia = ()
tupla_simples = (27,)

print(tupla[1])
print(tupla[3])


print()
for elemento in tupla:
    print(f"1 Elemento: {elemento}")

print()
for elemento in range(0, len(tupla)):
    print(f"2 Elemento: {tupla[elemento]} na posição {elemento}")

print()
for indice, elemento in enumerate(tupla):
    print(f"{indice}: {elemento}")

tupla_aninhada = ((1,2,3), 1, True, [1,4,'sim'])
print()
print(tupla_aninhada[0])
print(tupla_aninhada[1])
print(tupla_aninhada[2])
print(tupla_aninhada[3])
print(tupla_aninhada[3][2])

a, b, c, _, _ = tupla
print()
print(b)

print(len(tupla))
print(tupla.index(3.14))
print(tupla_direta.count("Edson"))

string = "Parisotto"
print(tuple(string))  # transforma uma string em uma tupla

print()
livro = tuple(["Fundação", "Isaac Asimov", "1949"])  # transforna uma lista em tupla
for i in livro:
    print(i)

filme1 = ("Duna", "2020")
filme2 = ("Blade Runner", "1990")
filmes = [filme1, filme2]

print()
for filme in filmes:
    titulo, ano = filme
    print(f"Filme: {titulo}\nAno: {ano}\n")

for filme in filmes:
    print(filme)

print()
materias = ("Matemática", "Física", "História", "Português")
for materia in materias:
    print(materia)

print()
for indice, materia in enumerate(materias):
    print(f"Índice: {indice}, Matéria: {materia}")

print()
print(materias)
for materia in materias:
    print(materia)