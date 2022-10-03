# PROGRAMA PARA COMPARAR NÚMEROS
num1 = int(input("\033[34mInsira o primeiro número: \033[m"))
num2 = int(input("Insira o segundo número: "))
if num1 > num2:
    print("\033[33mO primeiro valor é maior!")
elif num2 > num1:
    print("\033[33mO segundo valor é maior!")
else:
    print("\033[33mNão existe valor maior, os dois são iguais.")
