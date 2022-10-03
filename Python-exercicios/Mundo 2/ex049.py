# PROGRAMA DE TABUADA V.02
num = int(input("Digite um número para ver a sua tabuada: "))
print(f"A tabuada de {num} é:")
for c in range(1, 11):
    print(f"{num} x {c} = {num*c}")
