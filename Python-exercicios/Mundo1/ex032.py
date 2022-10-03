# PROGRAMA ANO BISSEXTO
from datetime import date
ano = int(input("Que ano quer analisar? Coloque 0 para o ano ano atual: "))
if ano == 0:
    ano = date.today().year  # Para pegar o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # divisivel por 4 E não divisivel por 100 ou divisivel por 400
    print(f"O ano {ano} é bissexto! ")
else:
    print(f"O ano {ano} não é bissexto! ")
