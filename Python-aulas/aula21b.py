def teste_local(b):
    a = 8
    b += 4
    c = 2
    print("Função teste local")
    print(f"A = {a}")
    print(f"B = {a}")
    print(f"C = {c}")
    print("=-" * 10)


def teste_global(b):
    global a
    a = 8
    b += 4
    c = 2
    print("Função teste global")
    print(f"A = {a}")
    print(f"B = {a}")
    print(f"C = {c}")
    print("=-" * 10)


# Programa principal
a = 2
teste_local(a)
print(f"A = {a}")
teste_global(a)
print(f"A = {a}")
