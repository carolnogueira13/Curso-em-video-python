# PROGRAMA MAIOR E MENOR VALORES
resp = "S"
cont = Soma = maior_valor = menor_valor = 0
while resp == "S":
    num = int(input("Digite um número: "))
    cont += 1
    Soma += num
    if cont == 1:
        maior_valor = menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        if num < menor_valor:
            menor_valor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()
print(f"Você digitou {cont} números e a média foi {Soma/cont:.2f}.")
print(f"O maior valor foi {maior_valor} e o menor valor foi {menor_valor}.")
