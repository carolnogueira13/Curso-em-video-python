# PROGRAMA PARA SORTEAR UM ALUNO
import random

aluno1 = input("Digite o primeiro aluno: ")
aluno2 = input("Digite o segundo aluno: ")
aluno3 = input("Digite o terceiro aluno: ")
aluno4 = input("Digite o quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]  # Para usar o random precisa criar uma lista
print("O aluno sorteado é {}".format(random.choice(lista)))
