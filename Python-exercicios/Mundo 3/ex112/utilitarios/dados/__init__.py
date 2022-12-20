def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO!\"{entrada}\" é um preço inválido!\033[m")
        else:
            return float(entrada)


def leiaInt(num):
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print("\033[31mERRO!Digite um número inteiro válido\033[m")

