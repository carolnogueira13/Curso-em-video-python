# PROGRAMA PARA PROGRESSÃO ARITMÉTICA V.01
print("--OS 10 PRIMEIROS TERMOS DE UMA P.A.--")
n = int(input("O PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
for c in range(n, n + (10*r), r):
    print(c, "-", end=" ")
print("ACABOU")
