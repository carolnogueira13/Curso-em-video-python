# PROGRAMA PARA CALCULAR ÍNDICE DE MASSA CORPORAL
peso = float(input("Qual o seu peso (em kg): "))
altura = float(input("Qual a sua altura: "))
IMC = peso/(altura ** 2)
print(f"O seu IMC é {IMC:.1f}. Isso representa que você está:", end=" ")
if IMC < 18.5:
    print("ABAIXO DO PESO normal, cuidado!")
elif IMC < 25:
    print("NO PESO IDEAL!")
elif IMC < 30:
    print("COM SOBREPESO!")
elif IMC < 40:
    print("COM OBESIDADE!")
else:
    print("COM OBESIDADE MORBIDA, cuidado!")