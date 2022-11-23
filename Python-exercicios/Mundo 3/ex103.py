# PROGRAMA FICHA DO JOGADOR
def ficha(nome="<desconhecido", gols=0):
    if nome == "":
        nome = "<desconhecido>"
    return f"O jogador {nome} fez {gols} gols no campeonato."


# Programa principal
jogador = str(input("Nome do Jogador: "))
n = str(input("Número de gols: "))
if n.isnumeric():  # para conferir se foi informado um número nos gols
    n = int(n)
else:
    n = 0
if jogador.strip() == "":  # se o campo jogador for vazio
    print(ficha(gols=n))
else:
    print(ficha(jogador, n))

