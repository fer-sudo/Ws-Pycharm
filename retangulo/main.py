import math

base : float
altura : float
area : float
perimetro : float
diagonal : float

base = float(input("base do retangulo: "))
altura = float(input("altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"valor da area = {area:.4f}")
print(f"valor do perimetro = {perimetro:.4f}")
print(f"valor da diagonal =  {diagonal:.4f}")