# PROGRAMA UM PRINT ESPECIAL
def escreva(text):
    tamanho = len(text)+4
    print("~" * tamanho)
    print(f"{text:^{tamanho}}")
    print("~" * tamanho)


# Programa principal
escreva("Gustavo Guanabara")
escreva("Curso de Python no Youtube")
escreva("CeV")
