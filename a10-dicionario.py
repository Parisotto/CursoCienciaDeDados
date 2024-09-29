# Dicionário
# dicionario = {chave:valor}
# dicionario = dict(chave1:valor1, chave2:valor2, ...)

dicionario = {} # cria dicionário vazio

dicionario["Cidade"] = "São Paulo"
dicionario["Estado"] = "SP"
dicionario["Região"] = "Sudeste"

print(dicionario)
print(dicionario["Cidade"])
print(dicionario.get("Estado"))
print(dicionario.get("ChaveInexistente", "Valor alternativo se chave não existir"))

dict_pessoa = dict(nome="Edson", idade=61, cidade="São Paulo")
print()
print(dict_pessoa)
for indice, (chave, valor) in enumerate(dict_pessoa.items(), start=1):
    print(f"{indice}) {chave}: {valor}")

dicionario_direto = {"pi":3.14, "phi":1.618, "e":2.72, "Raiz de 2": 1.42}
print()
for chave in dicionario_direto:
    valor = dicionario_direto[chave]
    print(f"{chave}: {valor}")

 
# Pegar todas as chaves e valores: método .items()
print()
for chave, valor in dicionario.items():
    print(chave, valor)

# Pegar só as chaves: método .key()
print()
for chave in dicionario.keys():
    print(chave)

# Pegar só os valores: método .values():
print()
for valor in dicionario.values():
    print(valor)

# EXEMPLOS:

contato = {
    'nome': 'Edson Parisotto',
    'telefone': '(11) 99999-9999',
    'email': 'edsonparisotto@prof.educacao.sp.gov.br',
    'idade': 61,
    'cidade': 'São Paulo'
}

notas = {
    'Alice': 95,
    'Amanda': 90,
    'Ana': 85,
    'Zaratrusta': 100
}

# Dicionário aninhados

biblioteca = {
    "L1": {"titulo":"O Nome da Rosa", "autor":'Umberto Eco'},
    "L2": {"titulo":"Estorvo", "autor":"Chico Buarque"},
    "L3": {"titulo":"Fundação", "autor":"Isaac Asimov"}
}

livro = "L1"
print(f"Leia {biblioteca[livro]['titulo']} de {biblioteca[livro]['autor']}!")

print()
novo_dicionario = dicionario.copy()
print(novo_dicionario)
valor = novo_dicionario.get('Estado', 'Chave não encontrada')
print(valor)
valor = novo_dicionario.get('País', 'Chave não encontrada')
print(valor)

print()
print(novo_dicionario)
valorRemovido = novo_dicionario.pop('Estado', 'Chave não encontrada') # removo um item
print(valorRemovido)
print(novo_dicionario)

print()
novo_dicionario.clear()
print(novo_dicionario)

# Compreensão de dicionários 
# novo_dicionário = {novo_valor expressão for elemento in lista_original if condissão}

print({x: x**2 for x in range(1, 6)})

quadrados_dict = {}
for x in range(1, 6):
    quadrados_dict[x] = x**2
print(quadrados_dict)

