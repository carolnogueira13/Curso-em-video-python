# PROGRAMA PARA PROCURAR UMA STRING DENTRO DE OUTRA
nome = str(input("Digite o seu nome completo: ")).strip()
silva = "silva" in nome.lower()
print(f"O seu nome tem Silva? {silva}")
