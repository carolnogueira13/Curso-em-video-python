# PROGRAMA PARA APLICAR DESCONTO EM UM PRODUTO
preço = float(input("Qual é o preço do produto? R$ "))
desconto = float(input("Qual o desconto do produto (responda em porcentagem): "))
novopreço = preço - ((desconto/100) * preço)
print("O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}." .format(preço, desconto, novopreço))
