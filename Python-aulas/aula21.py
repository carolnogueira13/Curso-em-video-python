def somar(a=0, b=0, c=0):  # Parâmetros opcionais o programa aceita de 0 a 3 parâmetros
    s = a + b + c
    print(f"A = {a}, B = {b} e C = {c}")
    print(f"A soma é {s}")


# Programa principal
somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()
somar(c=4, b=2)
