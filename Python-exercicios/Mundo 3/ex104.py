# PROGRAMA VALIDANDO ENTRADA DE DADOS EM PYTHON
def leiaInt(num):
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print("\033[31mERRO!Digite um número inteiro válido\033[m")


# Programa principal
número = leiaInt("Digite um número: ")
print(f"O número digitado foi {número}")
