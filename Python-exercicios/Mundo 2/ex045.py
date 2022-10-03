# PROGRAMA PARA JOGAR PEDRA, PAPEL E TESOURA
from time import sleep
from random import randint
itens = ("Pedra", "Tesoura", "Papel")
computador = randint(0, 2)
print("-"*10, "SE PREPARE PARA JOGAR JOKENPÔ", "-"*10)
escolha = int(input("""OPÇÕES DE JOGADA
\033[31m[ 0 ] PEDRA\033[m
\033[32m[ 1 ] TESOURA\033[m
\033[33m[ 2 ] PAPEL\033[m
QUAL A SUA JOGADA? """))
if escolha != 0 and escolha != 1 and escolha != 2:
    print("JOGADA ERRADA! Tente novamente!")
    exit()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!!!!")
sleep(1)
computador = randint(0, 2)
print("-"*40)
print(f"Você escolheu {itens[escolha]}")
print(f"O computador escolheu {itens[computador]}")
print("-"*40)

if escolha == 0:
    if computador == 0:
        print("EMPATE!")
    elif computador == 1:
        print("VOCÊ GANHOU!")
    else:
        print("VOCÊ PERDEU!")
elif escolha == 1:
    if computador == 0:
        print("VOCÊ PERDEU!")
    elif computador == 1:
        print("EMPATE!")
    else:
        print("VOCÊ GANHOU!")

elif escolha == 2:
    if computador == 0:
        print("VOCÊ GANHOU!")
    elif computador == 1:
        print("VOCÊ PERDEU!")
    else:
        print("EMPATE!")
