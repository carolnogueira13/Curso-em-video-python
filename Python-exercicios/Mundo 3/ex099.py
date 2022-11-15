# PROGRAMA QUE DESCOBRE O MAIOR
from time import sleep


def maiorvalor(* num):
    print("-=" * 30)
    print("Analisando os valores passados...")
    cont = maior = 0
    for c in num:
        if cont == 0:
            maior = c
        elif c > maior:
            maior = c
        cont += 1
        print(c, end=" ")
        sleep(0.25)
    print(f"Foram informados {len(num)} valores ao todo. ")
    print(f"O maior valor informado foi {maior}")
    sleep(0.5)


# Programa principal
maiorvalor(2, 9, 4, 5, 7, 1)
maiorvalor(4, 7, 0)
maiorvalor(1, 2)
maiorvalor(6)
maiorvalor()
