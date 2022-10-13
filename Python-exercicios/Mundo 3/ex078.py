# PROGRAMA PARA MOSTRAR O MENOR E O MAIOR VALOR DE UMA LISTA
numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f"Digite o valor da posição {c}: ")))
print("-"*70)
print(f"Você digitou os valores {numeros}")
print(f"O maior valor digitado foi {max(numeros)} e ele se encontra na posição ", end='')
for pos, c in enumerate(numeros):
    if c == max(numeros):
        print(f"{pos}...", end="")

print(f"\nO menor valor digitado foi {min(numeros)} e ele se encontra na posição ", end='')
for pos, c in enumerate(numeros):
    if c == min(numeros):
        print(f"{pos}...", end="")