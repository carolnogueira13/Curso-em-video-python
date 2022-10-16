pessoas = list()
individuo = list()
maior = menor = 0
while True:
    individuo.append(str(input("Nome: ")).strip())
    individuo.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = individuo[1]
    elif individuo[1] > maior:
        maior = individuo[1]
    elif individuo[1] < menor:
        menor = individuo[1]
    pessoas.append(individuo[:])
    individuo.clear()
    resp = str(input("Quer continuar? [S/N]")).upper()
    if resp == "N":
        break
print("-"*50)
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso é {maior} kg. O peso de", end=" ")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end= " ")
print(f"\nO menor peso é {menor} kg. O peso de", end=" ")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=" ")
