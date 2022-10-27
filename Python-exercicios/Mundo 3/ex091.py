# PROGRAMA JOGO DE DADOS EM PYTHON
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print("Valores sorteados")
for k,v in jogo.items():
    print(f"O {k} tirou o {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Sorted para ordenar, o itemgetter para
# saber através de qual item será ordenado (nesse o item da posição 1, ou seja, o randint) e o reverse
# True para deixar do maior para o menor
print("-"*40)
print("RANKING DOS JOGADORES")
for i,v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)



