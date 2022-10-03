# PROGRAMA DE ANÁLISE DE DADOS DO GRUPO
maiores = homens = mulheresnovas = 0
cont = 1
while True:
    print("-"*20)
    print(f"CADASTRE A {cont}ª PESSOA")
    print("-"*20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).upper()
    if idade >= 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheresnovas += 1
    cont += 1
    print("-" * 20)
    escolha = str(input("Quer continuar? [S/N] ")).upper()
    if escolha == "N":
        break
print("-" * 20)
print(f"Total de pessoas com mais de 18 anos: {maiores}")
print(f"Ao todo temos {homens} homens cadastrados. ")
print(f"E temos {mulheresnovas} mulheres com menos de 20 anos.")
