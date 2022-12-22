# TRATAMENTO DE ERROS
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:  # caso ocorrer a exceção vai para essa parte
    print(f"O problema encontrado foi {erro.__class__}")
else:  # caso não ocorrer a exceção vai para essa parte
    print(f"O resultado é {r}")
finally:  # em qualquer caso vai para essa parte
    print("Volte sempre! Muito obrigado!")
