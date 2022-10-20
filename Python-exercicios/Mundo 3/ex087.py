# PROGRAMA SOBRE MAIS MATRIZ EM PYTHON
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f"Digite o valor para [{c}, {l}]: "))
        if matriz[c][l] % 2 == 0:
            soma_pares += matriz[c][l]
        if l == 2:
            soma_coluna += matriz[c][l]

print("-" * 50)
for c in range(0, 3):
    for l in range(0, 3):
        print(f"[{matriz[c][l]:^5}]", end="")
    print()
print("-" * 50)
print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_coluna}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")
