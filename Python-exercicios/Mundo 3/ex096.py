# PROGRAMA FUNÇÃO QUE CALCULA A ÁREA
def area(lar, comp):
    a = lar * comp
    print(f"A área de um terreno de {lar}X{comp} é de {a}m².")


print("Controle de terrenos")
print("-" * 20)
largura = float(input("LARGURA(m): "))
comprimento = float(input("COMPRIMENTO(m): "))
area(largura, comprimento)
