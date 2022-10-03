# PROGRAMA DE NÚMEROS PRIMOS
n = int(input("Digite um número: "))
divisível = 0
for c in range(1, n+1):
    if n % c == 0:
        divisível += 1
        print(f"\033[34m{c}\033[m", end=" ")
    else:
        print(f"\033[31m{c}\033[m", end=" ")
print(f"\nO número {n} foi divisível {divisível} vezes.")
if divisível == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!")
