# input() e print()

nome = input("Digite seu nome: ")
idade = int(input("Digie sua idade: "))
altura = 1.8

print(nome)
print(idade)
print(f"Nome: {nome} - Idade: {idade}")

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
print(dia, mes, ano, sep='/')

print(f"Nome: {nome}", end=" - ")
print(f"Idade: {idade}", end=" ")
print(f"Altura: {altura:.2f}")

