# PROGRAMA PARA AUMENTOS MÚLTIPLOS
salario = float(input("Insira o valor do salário do funcinário: R$"))
if salario > 1250:
    salarionovo = salario + (0.1 * salario)
else:
    salarionovo = salario + (0.15 * salario)
print(f"Com o aumento, o novo salário do funcionário é R${salarionovo:.2f}")
