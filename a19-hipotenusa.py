# import math
from math import hypot

catetoOposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** 0.5

print(f"A hipotenusa mede {hipotenusa: .2f}")

hipo = hypot(catetoOposto, catetoAdjacente)
print(f"A hipotenusa mede {hipo: .2f}")
