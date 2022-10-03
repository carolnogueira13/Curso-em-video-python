# PROGRAMA RADAR ELETRÔNICO
velocidade = float(input("Digite a velocidade do carro (em km/h): "))
if velocidade > 80:
    print("Você foi multado, você excedeu o limite permitido de 80 km/h.")
    multa = 7 * (velocidade - 80)
    print(f"E o valor da multa é de R${multa:.2f}")
else:
    print("A velocidade do carro está de acordo com o permitido.")
