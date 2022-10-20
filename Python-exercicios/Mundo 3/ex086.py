# PROGRAMA MATRIZ EM PYTHON
matriz = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        matriz[c].append(int(input(f"Digite um valor para [{c},{d}]: ")))
print("-"*50)
for c in matriz:
    for n in c:
        print(f"[{n:^5}]", end="")
    print()
