# PROGRAMA PARA CALCULAR FATORIAL
"""n = int(input("Digite o número que ser saber o fatorial: "))
fatorial = 1
print(f"{n}! =", end=" ")
for c in range(n, 0, -1):
    fatorial = fatorial * c
    print(f"{c} X" if c > 1 else f"{c} =", end=" ")
print(fatorial)"""

n = int(input("Digite o número que ser saber o fatorial:"))
fatorial = 1
print(f"{n}! =", end=" ")
while n > 0:
    print(f"{n} X" if n > 1 else f"{n} =", end=" ")
    fatorial = fatorial * n
    n -= 1
print(fatorial)

"""import math
n = int(input("Digite o número que ser saber o fatorial:"))
f = math.factorial(n)
print(f"O fatorial de {n} é {f}")"""

