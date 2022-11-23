# PROGRAMA CÁLCULO DE FATORIAL
def fatorial(n, s=False):
    """
    -- Cálculo de fatorial
    :param n: Número a ser calculado
    :param s: (opcional) mostrar ou não a conta
    :return: O cálculo do fatorial de um número n
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if s:
            if c != 1:
                print(f"{c} * ", end="")
            else:
                print(f"{c} = ", end="")
    return fat


# Programa principal
print(fatorial(5))
print(fatorial(5, True))
help(fatorial)
