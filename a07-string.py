string = "Hello, world!"
for caracter in string:
    print(caracter)

for caracter in "Olá, mundo!":
    print(caracter)

print(string[7:12])
print("Olá, mundo!"[5:10])
print("Bom, dia!"[-1])

s1 = "Vamos"
s2 = "lá!"
print(s1 + " " + s2)
print(len("Tamanho de um texto."))

mensagem = "Tudo o que é sólido se desmancha no ar."
print("lid" in mensagem) # True
print("x" in mensagem) # False

# Fatiamento
slicing = mensagem[11:19] 
print(slicing) # "é sólido"

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace("o ar", "a atmosfera"))
print(" Hoje em dia.  ".replace(" ", ""))
