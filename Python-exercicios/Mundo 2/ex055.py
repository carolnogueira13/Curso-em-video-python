# PROGRAMA MAIOR E MENOR DA SEQUÊNCIA
pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}ª pessoa? "))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print(f"O maior peso lido foi de {pesomaior}kg.")
print(f"O menor peso lido foi de {pesomenor}kg.")
