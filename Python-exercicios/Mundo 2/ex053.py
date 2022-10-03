# PROGRAMA DETECTOR DE PALÍNDROMO
frase = str(input("Digite um frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)  # Para juntar todas as palavras da frase
inverso = junto[::-1]
'''inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f"A frase {junto} ao contrário fica {inverso}.")
if junto == inverso:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")
