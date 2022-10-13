# PROGRAMA LISTAS DE PREÇOS EM TUPLAS
listagem = ("Lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Tranferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 200,
            "Canetas", 22.30,
            "Livros", 35.90)
print("-"*45)
print(f"{'LISTAGEM DE PREÇOS':^45}") # Para o texto ficar centralizado em com o tamanho de 45 caracteres
print("-"*45)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f"{listagem[cont]:.<35}", end="") # Para o texto ficar com o tamanho de 35 caracteresc, alinhada a
        # esquerda e com o ponto
    else:
        print(f"R$ {listagem[cont]:7.2f}")
print("-"*45)