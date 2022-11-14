# APRIMORANDO OS DICIONÁRIOS
time = list()
jogador = dict()
gols = list()
while True:
    gols.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, partidas):
        gols.append(int(input(f"     Quantos gols na partida {c + 1}? ")))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)  # Função sum é o somatorio da lista gols
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()
        if resp in "S, N":
            break
        print("ERRO! Responda apenas S ou N")
    if resp == "N":
        break
print("-"*40)
print(f"{'cód ':<3}{'nome':<15}{'gols':<15}{'total'}")
print("-"*40)
for i,jogador in enumerate(time):
    print(f"{i:<3}", end=" ")
    for j in jogador.values():
        print(f"{str(j):<15}", end="")
    print()
print("-"*40)

while True:
    while True:
        busca = int(input("Mostrar dados de qual jogador? [999 para parar]"))
        if busca in [0, len(time) - 1] or busca == 999:
            break
        print(f"ERRO! Não existe jogador com o código {busca}")
    if busca == 999:
        break
    print(f"LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
    for p, c in enumerate(time[busca]['gols']):
        print(f"==> Na partida {p} fez {c} gols")
    print("-"*40)
print("VOLTE SEMPRE!")
