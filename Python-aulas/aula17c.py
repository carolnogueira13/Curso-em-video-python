a = [2, 3, 4, 5]
b = a # Cria uma ligação. A partir do momento em que você iguala as listas tudo que você fizer com uma irá refletir
# na outra
c = a[:] # Cria uma cópia de a, somente copia os valores de a no momento
print(f"A lista A é: {a}")
print(f"A lista B é: {b}")
print(f"A lista C é: {c}")
a[0] = 6 # Esse comando mudou a posição 2 da lista B também, mas não mudou na C que é só uma cópia de A
print(f"A lista A é: {a}")
print(f"A lista B é: {b}")
print(f"A lista C é: {c}")