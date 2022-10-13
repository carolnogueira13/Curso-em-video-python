# PROGRAMA MAIOR E MENOS VALORES NO TUPLA
from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores sorteados foram: ", end="")
for n in lista:
    print(n, end=" ")
"""lista_ordenada = sorted(lista)
print(f"\nO menor valor sorteado foi {lista_ordenada[0]}")
print(f"O maior valor sorteado foi {lista_ordenada[4]}")"""
print(f"\nO menor valor sorteado foi {min(lista)}") # Retorna o menor valor da lista
print(f"O menor valor sorteado foi {max(lista)}") # Retorna o maior valor da lista
