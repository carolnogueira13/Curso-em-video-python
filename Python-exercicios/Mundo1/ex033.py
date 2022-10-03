# PROGRAMA MAIOR E MENOR VALORES
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))
# Verificando o maior valor
maior = num1
if num2 > num3 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3
# Verificando o menor valor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f"O menor número é {menor} e o maior número é {maior}!")
