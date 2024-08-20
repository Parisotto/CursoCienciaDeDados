import math as m
from pandas import DataFrame
import scipy

raiz = m.sqrt(9)
print(f"A raiz quadrada é {raiz}")

print(m.ceil(6.1))

dados = {'Nome': ['Alice','Beto','Carlos'],'Idade':[25,30,35]}
dadosFormatados = DataFrame(dados)
print(dadosFormatados)

# PARA INSTALAR O PANDAS E O SCIPY DIGITE NO TERMINAL:
# pip download pandas 
# pip download scipy
# teste