# PROGRAMA ESTATÍSTICAS EM PRODUTOS
total = produtocaro = preçobarato = 0
barato = " "
cont = 1
print("LOJAS AC")
print("-"*20)
while True:
    print(f"{cont}º PRODUTO:")
    nome = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    resp = str(input("Quer continuar? [S/N] ")).upper()
    total += preço
    if preço > 1000:
        produtocaro += 1
    if cont == 1 or preço < preçobarato:
        preçobarato = preço
        barato = nome
    cont += 1
    print("-"*20)
    if resp == "N":
        break
print(f"O total da compra foi R${total:.2f}.")
print(f"Temos {produtocaro} produtos custando mais que R$1000,00")
print(f"O produto mais barato foi {barato} que custa R${preçobarato:.2f}.")
