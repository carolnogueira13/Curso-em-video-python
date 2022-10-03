# PROGRAMA PARA PROGRESSÃO ARITMÉTICA V.02
print("--OS 10 PRIMEIROS TERMOS DE UMA P.A.--")
n = int(input("O PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
termo = n
while termo <= n + (9*r):
    print(f"{termo} -", end=" ")
    termo += r
print("FIM")
