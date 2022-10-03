# PROGRAMA JOGO DE ADIVINHAÇÃO V.02
import random
from time import sleep
print("-" * 60)
print("Vou pensar em um número entre O e 10. Tente adivinhar...")
print("-" * 60)
computador = random.randint(0, 10)  # Faz o computador "PENSAR"
jogador = int(input("\nEm que número eu pensei? "))  # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(1)  # Para o programa por 1 segundo
tentativas = 1
while jogador != computador:
    if computador > jogador:
        jogador = int(input("Mais...Tente digitar outro número: "))
    else:
        jogador = int(input("Menos...Tente digitar outro número: "))
    tentativas += 1
    print("PROCESSANDO...")
    sleep(1)
print(f"Parabéns você acertou depois de {tentativas} tentativas.")
