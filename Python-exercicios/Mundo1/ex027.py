# PROGRAMA PARA LER O PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA
n = str(input("Digite o seu nome completo: ")).strip()
nome = n.split()
print("Prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}.")
print(f"Seu último nome é {nome[-1]}.")  # O nome[-1] retorna a última posição da lista
