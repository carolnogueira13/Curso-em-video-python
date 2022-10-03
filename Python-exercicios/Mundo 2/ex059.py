# PROGRAMA CRIANDO UM MENU DE OPÇÕES
from time import sleep
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
resp = "0"
while resp != "5":
    resp = str(input("""--------------------------------
    [1] Somar os números
    [2] Multiplicar os números
    [5] Sair do programa
    [3] Saber qual deles é maior
    [4] Novos números
>>>>Insira a sua opção: """))
    if resp == "1":
        print(f"\n{num1} + {num2} =  {num1 + num2}")
    elif resp == "2":
        print(f"\n{num1} X {num2} = {num1 * num2}")
    elif resp == "3":
        if num1 > num2:
            print(f"\nEntre {num1} e {num2}, o maior valor é {num1}")
        elif num2 > num1:
            print(f"\nEntre {num1} e {num2}, o maior valor é {num2}")
        else:
            print("\nOs números são iguais!")
    elif resp == "4":
        print("\nInforme os números novamente:")
        num1 = float(input("Primeiro valor: "))
        num2 = float(input("Segundo valor: "))
    elif resp == "5":
        print("Finaiizando...")
    else:
        print("\nOpção inválida. Digite uma opção válida ou 5 para sair")
    sleep(1)
print("Fim do programa.Volte sempre!")
