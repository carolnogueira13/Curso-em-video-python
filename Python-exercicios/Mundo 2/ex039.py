# PROGRAMA DE ALISTAMENTO MILITAR
from datetime import date
sexo = str(input("Insira o seu gênero (F para feminino , M para Masculino e "
                 "N para não identificado):  "))
if sexo == "M":
    ano = int(input("Digite o seu ano de nascimento: "))
    idade = date.today().year - ano
    print(f"Quem nasceu em {ano} tem {idade} anos em {date.today().year}.")
    if idade < 18:
        print(f"Ainda faltam {18 - idade} anos para se alistar.")
        print(f"Seu alistamento será em {ano + 18}.")
    elif idade > 18:
        print(f"Já passaram {idade - 18} anos do seu alistamento.")
        print(f"Seu alistamento deveria ter sido feito em {ano + 18}")
    else:
        print("Deve se alistar IMEDIATAMENTE!")
else:
    print("Você não precisa de alistar.")
