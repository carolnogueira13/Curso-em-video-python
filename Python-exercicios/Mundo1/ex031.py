# PROGRAMA PARA CALCULAR CUSTO DA VIAGEM
distancia = float(input("Qual a distância da sua viagem (em km)? "))
passagem = 0.5 * distancia if distancia <= 200 else 0.45 * distancia
"""if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia"""
print(f"O preço da passagem para a viagem é R${passagem:.2f}")
