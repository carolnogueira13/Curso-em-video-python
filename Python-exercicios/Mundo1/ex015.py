# PROGRAMA PARA ALUGUEL DE CARROS
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
total = (60 * dias) + (0.15 * km)
print("O total a pagar é de R${:.2f}." .format(total))

