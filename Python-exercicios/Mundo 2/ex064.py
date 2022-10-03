# PROGRAMA TRATANDO DE VÁRIOS VALORES V.01
n = int(input("Digite um número [999 para parar]: "))
números = Soma = 0
while n != 999:
    números += 1
    Soma += n
    n = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {números} números e a soma entre eles foi {Soma}.")
