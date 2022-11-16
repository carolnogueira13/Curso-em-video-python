def função():
    n1 = 4  # variável com escopo local (dentro da função)
    print(f"N1 dentro vale {n1}")


# Programa principal
n1 = 2  # variável com escopo global (dentro do programa principal)
função()
print(f"N1 fora vale {n1}")
