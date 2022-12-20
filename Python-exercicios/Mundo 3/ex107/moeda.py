def aumentar(preço, n):
    res = preço + (preço * (n / 100))
    return res


def diminuir(preço, n):
    res = preço - (preço * (n / 100))
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço * (1 / 2)
    return res
