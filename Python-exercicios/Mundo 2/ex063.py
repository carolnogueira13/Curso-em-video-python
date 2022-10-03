# PROGRAMA SEQUÊNCIA DE FIBONACCI V.01
print("Sequência de Fibonacci")
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} - {t2} -", end=" ")
cont = 3
while cont <= n:
    S = t2 + t1
    print(f"{S} - ", end="")
    t1 = t2
    t2 = S
    cont += 1
print("FIM")
