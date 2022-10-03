# PROGRAMA PARA CALCULAR O PREÇO DE UM PRODUTO CONSIDERANDO A CONDIÇÃO DE PAGAMENTO
preço_inicial = float(input("Qual o preço das compras? R$ "))
condição = str(input("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção? """))

if condição == "1":
    preço = preço_inicial - (0.1 * preço_inicial)
    print("Para o pagamentos à vista, o cliente recebe um desconto de 10% e o preço "
          f"total fica R${preço:.2f}")
elif condição == "2":
    preço = preço_inicial - (0.05 * preço_inicial)
    print("Para o pagamentos à vista no cartão, o cliente recebe um desconto de "
          f"5% e o preço total fica R$ {preço:.2f}")
elif condição == "3":
    print("Para o pagamentos no cartão em 2 vezes, o preço total se mantém o mesmo de "
          f"R$ {preço_inicial:.2f} e você irá pagar duas parcelas de R${preço_inicial/2:.2f} sem juros.")
elif condição == "4":
    parcelas = int(input("Quantas parcelas? "))
    preço = preço_inicial + (0.2 * preço_inicial)
    print(f"Para pagamentos no cartão de {parcelas} vezes, o cliente recebe 20% de juros, então"
          f" o preço total fica R${preço:.2f} e ele irá pagar {parcelas} de "
          f"R${preço/parcelas:.2f}")
else:
    print("Você digitou uma opção inválida de pagamento.")
