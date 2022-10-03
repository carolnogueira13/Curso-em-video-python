# PROGRAMA AQUELE CLÁSSICO DA MÉDIA
nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
media = (nota1 + nota2)/2
if media >= 7.0:
    print(f"A média do aluno é {media:.1f} e ele está: \033[32mAPROVADO!")
elif 6.9 > media >= 5.0:
    print(f"A média do aluno é {media:.1f} e ele está em: \033[34mRECUPERAÇÃO!")
else:
    print(f"A média do aluno é {media:.1f} e ele está: \033[31mREPROVADO!")