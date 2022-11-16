# PROGRAMA FUNÇÃO DE CONTADOR
from time import sleep


def contagem(i, f, p):
    """
    --> Faz uma contagem e mostra na tela 
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem returno
    Função criada por Ana Caroline
    """
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=" ")
            sleep(0.25)
        print("FIM")
    elif i > f:
        for c in range(i, f-1, -p):
            print(c, end=" ")
            sleep(0.25)
        print("FIM")
    else:
        print("Não há contagem pois o valor do início e do fim são iguais.")


def linha():
    print("-=" * 20)


# Programa principal
help(contagem)
contagem(1, 10, 1)
linha()
contagem(10, 0, 2)
linha()
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("INÍCIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))
linha()
contagem(inicio, fim, passo)
