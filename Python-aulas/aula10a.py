n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
print(f"A média do estudante é {media:.1f}!")
if media >= 6:
    print("Você está aprovado!")
else:
    print("Você está reprovado!")
