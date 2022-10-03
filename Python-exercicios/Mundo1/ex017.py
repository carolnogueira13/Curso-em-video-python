# PROGRAMA PARA CALCULAR A HIPOTENUSA DO TRIÂNGULO
import math
CatetoOposto = float(input("Comprimento do cateto oposto: "))
CatetoAdjacente = float(input("Comprimento do cateto adjacente: "))
print("A hipotenusa vai medir {:.2f}." .format(math.hypot(CatetoAdjacente, CatetoOposto)))
