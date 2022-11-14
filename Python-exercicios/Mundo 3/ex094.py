# PROGRAMA PARA UNIR DICIONÁRIOS E LISTAS
pessoa = dict()
pessoas = list()
idades = 0

# Leitura dos dados
while True:
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper()
        if pessoa['sexo'] in "M,F":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    idades += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()
        if resp in "S, N":
            break
        print("ERRO! Responda apenas S ou N")
    if resp == "N":
        break

# Analisando os dados
print("-" * 40)
print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas")
print(f"B) A média de idades é de {idades / len(pessoas):.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end="")
for pessoa in pessoas:
    if pessoa['sexo'] == "F":
        print(f"{pessoa['nome']}", end=" ")
print("\nD) Lista das pessoas que estão acima da média: ")
for pessoa in pessoas:
    if pessoa['idade'] >= idades / len(pessoas):
        for c, v in pessoa.items():
            print(f"{c} = {v}; ", end="")
        print()
print("<<ENCERRADO>>")
