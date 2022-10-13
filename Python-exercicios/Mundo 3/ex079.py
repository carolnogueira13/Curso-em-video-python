# PROGRAMA VALORES ÚNICOS EM UMA LISTA
lista = list()
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não será adicionado...")
    resp = str(input("Quer continuar?[S/N] ")).strip().upper()
    if resp == "N":
        break
print("-"*50)
lista.sort()
print(f"Você digitou os valores {lista}")
