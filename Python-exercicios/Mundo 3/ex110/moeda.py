def resumo(preço=0, taxa1=10, taxa2=5):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-"*30)
    print(f"Preço analisado: \t{moeda(preço)}")
    print(f"Dobro do preço: \t{dobro(preço,True)}")
    print(f"Metade do preço: \t{metade(preço, True)}")
    print(f"{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}")
    print(f"{taxa2}% de redução: \t{diminuir(preço,taxa2, True)}")
    print("-" * 30)


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
