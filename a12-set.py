# Set (conjunto)
# conjunto = {1,2,...} # não considera repetições

conjunto = {1, 2, 3, 3, 4, 5, 6, 7, 5, 4}
print(conjunto)

conjunto.add(9)
conjunto.remove(3)
print(conjunto)

outro_conjunto = {7, 5, 3, 9, 13}
uniao = conjunto.union(outro_conjunto)
intersecao = conjunto.intersection(outro_conjunto)
diferenca = conjunto.difference(outro_conjunto)

print()
print(uniao)
print(intersecao)
print(diferenca)

uniao = conjunto | outro_conjunto
intersecao = conjunto & outro_conjunto
diferenca = conjunto - outro_conjunto

# pip install matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,5))
ax.set_title("Operações de Conjuntos")
ax.set_xlabel("Elementos")
ax.set_ylabel("Conjuntos")
ax.set_yticks([1,2,3])
ax.set_yticklabels(["Conjunto 1", "Conjunto 2", "Operações"])
ax.scatter(list(conjunto), [1]*len(conjunto), color="blue", label="Conjunto 1")
ax.scatter(list(outro_conjunto), [2]*len(outro_conjunto), color="red", label="Conjunto 2")
ax.scatter(list(uniao), [3]*len(uniao), color="green", label="União", s=100)
ax.scatter(list(intersecao), [3]*len(intersecao), color="orange", label="Interseção")
ax.scatter(list(diferenca), [3]*len(diferenca), color="yellow", label="Diferença")
ax.legend()
plt.show()

