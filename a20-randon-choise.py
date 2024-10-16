import random

nomes = []
n = 5
while len(nomes) < n:
    resp = input(f"Digite {len(nomes) + 1}° nome: ")
    nomes.append(resp)

nomeSorteado = random.choice(nomes)
print(f"{nomeSorteado} foi o nome sorteado!")

random.shuffle(nomes)
print(nomes)
