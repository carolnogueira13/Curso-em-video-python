# PROGRAMA DO JOGO PAR OU ÍMPAR
from random import randint
print("VAMOS JOGAR PAR OU ÍMPAR")
cont = 0
while True:
    print("-" * 30)
    jogador = int(input("Digite um valor: "))
    escolha = " "
    while escolha not in "PI":
        escolha = str(input("Par ou ímpar? [P/I] ")).upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    if soma % 2 == 0:
        result = "PAR"
    else:
        result = "IMPAR"
    print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} deu {result}.")
    print("-" * 30)
    if result[0] == escolha:
        cont += 1
        print("VOCÊ VENCEU!")
        print("Vamos jogar novamente...")
    else:
        break
print("VOCÊ PERDEU!")
print(f"Game over! Você venceu {cont} vezes!")
