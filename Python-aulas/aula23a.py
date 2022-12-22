try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b
except (TypeError, ValueError):
    print("Tivemos um problema com os tipos de dados que você digitou!")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
else:
    print(f"O resultado é {r}")
