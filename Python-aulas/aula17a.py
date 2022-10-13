valores = [] # Cria uma lista vazia, tb poderia ser assim: valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f"{v}...", end="")

for pos, v in enumerate(valores):
    print(f"\nNa posição {pos} encontrei o valor {v}!") # Mostra a posição e o elemento