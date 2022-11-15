def contador(*num):  # desempacotamento
    print(f"Recebi os valores {num} e são ao todo {len(num)} números")
    for valor in num:
        print(valor, end=" ")
    print("FIM!")


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
