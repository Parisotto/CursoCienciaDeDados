# Tupla
# tupla = (elemento1, elemento2, ...)

tupla = (1, "Olá", 3.14, True, 'c') # uma tupla é imutável

tupla_direta = 0, "Edson", 1.618, 'p', "Edson"
tupla_vazia = ()
tupla_simples = (27,)

print(tupla[1])
print(tupla[3])

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
print(tuple(string))
