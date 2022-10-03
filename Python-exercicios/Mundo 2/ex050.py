# PROGRAMA PARA A SOMA DOS SEIS NÚMEROS LIDOS, APENAS PARES
S = 0
for c in range(0, 6):
    num = int(input("Digite o seu número: "))
    if num % 2 == 0:
        S += num
print(f"As soma dos números pares digitados é {S}.")
