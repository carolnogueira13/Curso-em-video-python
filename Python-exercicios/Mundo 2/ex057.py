# PROGRAMA VALIDAÇÃO DE DADOS
sexo = str(input("Informe seu sexo: [F/M] ")).strip().upper()
while sexo != "F" and sexo != "M":
    print("Dados inválidos!", end="")
    sexo = str(input("Por favor digite um sexo válido: ")).upper().upper()
print(f"Ok, o sexo {sexo} foi registrado com sucesso!")
