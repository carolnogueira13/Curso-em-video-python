# PROGRAMA PALPITES PARA A MEGA-SENA
from random import randint
from time import sleep
lista = list()
jogos = list()
print("     JOGO DA MEGA-SENA     ")
resp = int(input("Quantos jogos você quer que eu sorteie? "))
total = 1
while total <= resp:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f"SORTEANDO {resp} JOGOS DA MEGA-SENA")
for p, j in enumerate(jogos):
    sleep(0.5)
    print(f"Jogo {p+1} : {j}")



