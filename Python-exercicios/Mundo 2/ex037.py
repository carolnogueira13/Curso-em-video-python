# PROGRAMA CONVERSOR DE BASES NUMÉRICAS
num = int(input("Insira um número inteiro: "))
opção = str(input("""Escolha uma das bases para converter esse número:
1 - binário, 
2 - octal, 
3 - hexadecimal
Sua opção é: """))  # Três aspas para várias linhas
if opção == "1":
    print(f"O número {num} em binário é {num:b}")  # :b função embutida de bin()
elif opção == "2":
    print(f"O número {num} em binário é {num:o}")  # :o função embutida de oct()
elif opção == "3":
    print(f"O número {num} em binário é {num:x}")  # :x função embutida de hex()
else:
    print("Opção inválida!")
