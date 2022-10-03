# PROGRAMA PARA PROGRESSÃO ARITMÉTICA V.03
print("--TERMOS DE UMA P.A.--")
n = int(input("O PRIMEIRO TERMO: "))
r = int(input("RAZÃO: "))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -", end=" ")
        termo += r
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer a mais? "))
print(f"Progressão finalizado com {total} termos mostrados.")



