import math         # abreviação de mathematics
import math as m    # m é um apelido (alias) para math
from math import trunc

num = float(input("Digite um numero decimal: "))

print(trunc(9.45678))
print(f"O valor digitado foi {num} e a sua parte inteira é {trunc(num)}")
print(m.floor(num))
print(m.ceil(num))
print(round(num))
print(int(num))
