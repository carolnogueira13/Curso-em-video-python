# PROGRAMA NÚMERO POR EXTENSO
extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
       "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis",
       "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while num < 0 or num > 20:
        num = int(input("Número inválido! Digite um número de 0 a 20: "))
    print(f"Você digitou o número {extenso[num]}.")
    resp = str(input("Você deseja continuar a inserir números? [S/N] "))
    if resp == "N":
        break
print("Fim!")
