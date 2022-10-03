s = 0
while True:
    n = int(input("Digite um número: [999 para parar] "))
    if n == 999:
        break  # Comando para interromper o loop
    s += n
print(f"A soma vale {s}.")
