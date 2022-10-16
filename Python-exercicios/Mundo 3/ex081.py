# PROGRAMA EXTRAINDO DADOS DE UMA LISTA
lista = list()
while True:
    lista.append(int(input("Digite um número: ")))
    resp = str(input("Deseja digitar mais um número? [S/N] ")).strip().upper()
    if resp == "N":
        break
lista.sort(reverse=True)
print("-"*50)
print(f"Essa lista tem {len(lista)} elementos.")
print(f"A ordem dos elementos dessa lista em ordem descrescente fica: {lista}")
if 5 in lista:
    print("Essa lista contém o número 5.")
else:
    print("Essa lista não contém o número 5.")