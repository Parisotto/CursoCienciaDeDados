import math as m
import random

from pandas import DataFrame
import scipy

# PARA INSTALAR O PANDAS, O SCIPY DIGITE NO TERMINAL:
# pip download pandas
# pip download scipy

raiz = m.sqrt(9)
print(f"A raiz quadrada é {raiz}")
print(m.ceil(6.1))
print()

'''
num = int(input("Digite um número: "))
raiz = m.sqrt(num)
print(f'A raiz de {raiz} é igual a {raiz}')
print(f'A raiz de {raiz} é igual a {raiz:.3f}')
print(f'A raiz de {raiz} é igual a {m.ceil(raiz):.1f}')
print(f'A raiz de {raiz} é igual a {m.floor(raiz)}')
print()
'''

num = random.random()
print(num)
print(f"{num:.3f}")
print(f"{num * 10:.3f}")
print(f"{num * 100:.3f}")
print(f"{m.ceil(num * 100)}")
print(f"{m.floor(num * 100)}")
print(f"{m.floor(num * 100):.3f}")
print()

inteiro = random.randint(1, 10)
print(inteiro)
print()

dados = {'Nome': ['Alice','Beto','Carlos'],'Idade':[25,30,35]}
dadosFormatados = DataFrame(dados)
print(dadosFormatados)
print()

