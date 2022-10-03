# PROGRAMA ANALISANDO TRIÂNGULO V.01
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 > 0 and r2 > 0 and r3 > 0:
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print(f"Os segmentos {r1}, {r2} e {r3} formam um triângulo!")
    else:
        print("Os segmentos informados não formam um triângulo!")
else:
    print("Os segmentos informados não formam um triângulo!")
