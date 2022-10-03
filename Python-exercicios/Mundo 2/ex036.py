# PROGRAMA APROVANDO EMPRÉSTIMO
casa = float(input("Qual o valor da casa que pretende comprar? R$ "))
salario = float(input("Qual o valor do seu salário? R$ "))
tempo = int(input("Em quantos anos você pretende comprar a casa? "))
prestação = casa / (tempo * 12)
print(f"Para pagar uma casa de R$ {casa:.2f} em {tempo} anos, "
      f"o valor da prestação é de R${prestação:.2f}")
if prestação > (0.3 * salario):
    print("Empréstimo bancário negado.")
else:
    print("Empréstimo bancário aprovado.")
