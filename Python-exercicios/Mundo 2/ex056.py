# PROGRAMA PARA LER O NOME, A IDADE E O SEXO DE 4 PESSOAS
# NO FINAL DO PROGRAMA MOSTRE A MÉDIA DE IDADE DO GRUPO, O NOME DO HOMEM MAIS VELHO E
# QUANTAS MULHERES TEM MENOS DE 20 ANOS.
media = 0
maior_idade = 0
nome_do_mais_velho = ""
menos_de_20 = 0
for c in range(1, 5):
    nome = str(input(f"Qual o nome da {c}ª pessoa? ")).strip()
    idade = int(input(f"Qual a idade da {c}ª pessoa? "))
    sexo = str(input(f"Qual o gênero da {c}ª pessoa (F ou M)? ")).strip()
    print("-------------------------------------------------------------------------")
    media += idade
    if sexo in "Mm" and idade > maior_idade:
        nome_do_mais_velho = nome
        maior_idade = idade
    if sexo in "Ff" and idade < 20:
        menos_de_20 += 1
print(f"A média de idade do grupo é {media/4}")
print(f"O homem mais velho tem {maior_idade} anos e se chama {nome_do_mais_velho}.")
print(f"Ao todo são {menos_de_20} mulheres com menos de 20 anos.")
