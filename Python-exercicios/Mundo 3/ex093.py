# PROGRAMA CADASTRO DE JOGADOR DE FUTEBOL
jogador = dict()
gols = list()
jogador['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for c in range(0, partidas):
    gols.append(int(input(f"     Quantos gols na partida {c}? ")))
jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)  # Função sum é o somatorio da lista gols
print("-" * 50)
print(jogador)
print("-" * 50)
for c, v in jogador.items():
    print(f"O campo {c} tem valor {v}")
print("-" * 50)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for p, c in enumerate(jogador['gols']):
    print(f"==> Na partida {p} fez {c} gols")
print(f"Foi um total de {jogador['total']} gols")
