# PROGRAMA QUE FAÇA A SOMA DE ÍMPARES MÚLTIPLOS DE TRÊS DE 1 A 500
soma = 0
v = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
        v += 1
print(f"A soma dos {v} valores solicitados é {soma}.")
