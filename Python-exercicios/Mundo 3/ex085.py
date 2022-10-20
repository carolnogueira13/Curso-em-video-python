# PROGRAMA DE LISTAS DE NÚMEROS PARES E ÍMPARES
lista = [[], []]
for cont in range(1, 8):
    n = int(input(f"Digite um {cont}º valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print("-" * 50)
print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}")
