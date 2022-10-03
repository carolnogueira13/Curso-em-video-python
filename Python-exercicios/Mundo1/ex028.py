# PROGRAMA JOGO DE ADIVINHAÇÃO V.01
import random
from time import sleep
print("-" * 60)
print("Vou pensar em um número entre O e 5. Tente adivinhar...")
print("-" * 60)
computador = random.randint(0, 5)  # Faz o computador "PENSAR"
jogador = int(input("\nEm que número eu pensei? "))  # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)  # Para o programa por 2 segundos
if jogador == computador:
    print("PARABÉNS! Você conseguiu vencer!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")
