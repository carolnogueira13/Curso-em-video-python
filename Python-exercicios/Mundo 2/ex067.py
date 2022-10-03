# PROGRAMA TABUADA V.03
s = 0
while True:
    num = int(input("Quer ver a tabuada de que valor? "))
    print("-"*20)
    if num < 0:
        break
    for cont in range(1, 11):
        s = num * cont
        print(f"{num} X {cont} = {s}")
    print("-"*20)
print("PROGRAMA TABUADA ENCERRADO! Volte sempre!")