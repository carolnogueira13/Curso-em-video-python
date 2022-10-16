galera = list()
dado = list()
maiores = menores = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")).strip())
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 21:
        print(f"{p[0]} é maior de idade.")
        maiores += 1
    else:
        print(f"{p[0]} é menor de idade.")
        menores += 1
print(f"O total de maiores são {maiores} pessoas e menores são {menores} pessoas.")
