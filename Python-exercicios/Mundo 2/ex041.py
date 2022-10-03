# PROGRAMA CLASSIFICANDO ATLETAS
import datetime
ano = int(input("Insira o ano de nascimento do atleta: "))
idade = datetime.date.today().year - ano
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("E faz parte da categoria MIRIM!")

elif idade <= 14:
    print("E faz parte da categoria INFANTIL!")

elif idade <= 19:
    print("E faz parte da categoria JUNIOR!")

elif idade <= 25:
    print("E faz parte da categoria SÊNIOR!")

else:
    print("E faz parte da categoria MASTER!")
