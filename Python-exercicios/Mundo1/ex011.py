# PROGRAMA PARA CALCULAR A ÁREA DE PINTURA DE UMA PAREDE
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²." .format(largura, altura, area))
tinta = area/2 # Cada litro de tinta pinta 2m²
print("Para pintar essa parede, você precisará de {}l de tinta." .format(tinta))
