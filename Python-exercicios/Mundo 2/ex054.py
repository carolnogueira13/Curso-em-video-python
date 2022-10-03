# PROGRAMA PARA CALCULAR A MAIORIDADE DE 7 PESSOAS
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f"Digite o ano do seu nascimento da {c}ª pessoa: "))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"Nesse grupo de pessoas informados existem \033[31m{maior}\033[m pessoas "
      f"maiores de idade e \033[32m{menor}\033[m pessoas menores de idade.")
