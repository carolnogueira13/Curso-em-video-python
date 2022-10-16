# PROGRAMA DIVIDINDO VALORES EM VÁRIAS LISTAS
valores = []
pares = []
impares = []
while True:
    valores.append(int(input("Diqite um número: ")))
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()
    if resp == "N":
        break
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("-"*50)
print(f"A lista completa é : {valores}")
print(f"Os elementos pares da lista são: {pares}")
print(f"Os elementos ímpares da lista são: {impares}")

