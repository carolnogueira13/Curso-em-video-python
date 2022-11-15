# PROGRAMA COM FUNÇÕES PARA SORTEAR E SOMAR
from random import randint
from time import sleep


def sorteio(l):
    print("Sorteando 5 valores da lista: ", end="")
    for c in range(5):
        sort = randint(0, 10)
        l.append(sort)
        print(sort, end=" ")
        sleep(0.25)
    print("PRONTO!")


def somapares(l):
    soma = 0
    print(f"Somando os valores pares de {l}, temos ", end="")
    for valor in l:
        if valor % 2 == 0:
            soma += valor
    print(soma)


# Programa principal
numeros = list()
sorteio(numeros)
somapares(numeros)
