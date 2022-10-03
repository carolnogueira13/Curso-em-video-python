# PROGRAMA ANALISADOR DE TEXTO
nome = str(input("Digite o seu nome completo: ")).strip()
print("O seu nome em maiúsculas é {}" .format(nome.upper()))
print("O seu nome em minúculas é {}" .format(nome.lower()))
print("O seu nome ao todo tem {} letras" .format(len(nome) - nome.count(" ")))
# print("Seu primeiro nome tem {} letras" .format(nome.find(" ")))
dividido = nome.split()
print("O seu primeiro nome é {} e ele tem {} letras" .format(dividido[0], len(dividido[0])))





