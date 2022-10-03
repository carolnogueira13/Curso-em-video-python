# PROGRAMA ANALISANDO TRIÂNGULOS V.02
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print(f"Os segmentos {r1}, {r2} e {r3} formam um triângulo equilátero!")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print(f"Os segmentos {r1}, {r2} e {r3} formam um triângulo isósceles!")
    else:
        print(f"Os segmentos {r1}, {r2} e {r3} formam um triângulo escaleno!")
else:
    print("Os segmentos informados não formam um triângulo!")

