# PROGRAMA PARA FUNÇÕES APROFUNDADAS EM PYTHON
def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
        except KeyboardInterrupt:
            print("\nO usuário preferiu não inserir dados!")
            return 0
        except (TypeError, ValueError):
            print("Por favor! Digite um número inteiro válido!")
        else:
            return valor


def leiaFloat(num):
    while True:
        try:
            valor = float(input(num))
        except KeyboardInterrupt:
            print("\nO usuário preferiu não inserir dados!")
            return 0
        except (TypeError, ValueError):
            print("Por favor! Digite um número real válido!")
        else:
            return valor


# Programa principal:
numero = leiaInt("Digite um número inteiro: ")
numero2 = leiaFloat("Digite um número real: ")
print(f"Você digitou o número inteiro {numero} e o real {numero2}")
