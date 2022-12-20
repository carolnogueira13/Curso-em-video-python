def moeda(r=0, moeda="R$"):
    return f"{moeda}{r:.2f}".replace(".", ",")


def aumentar(preço=0, n=0, resp=False):
    res = preço + (preço * (n / 100))
    if resp:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, n=0, resp=False):
    res = preço - (preço * (n / 100))
    if resp:
        return moeda(res)
    else:
        return res


def dobro(preço=0, resp=False):
    res = preço * 2
    if resp:
        return moeda(res)
    else:
        return res


def metade(preço=0, resp=False):
    res = preço * (1 / 2)
    if resp:
        return moeda(res)
    else:
        return res
