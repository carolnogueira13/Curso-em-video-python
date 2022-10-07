lanche = ("Hambúrger", "Suco", "Pizza", "Pudim")
# Elemento 0: Hamburger; elemento 1: Suco; elemento 2: Pizza; elemento 3: Pudim
# Tuplas são imutáveis
print(lanche)
print(lanche[2])
print(lanche[-1])
print(lanche[1:])
print(lanche[1:3]) # Desconsidera o último elemento
print(lanche[:2])
print(lanche[-3:])
print(sorted(lanche)) #Colocar a tupla em ordem

# 1ª forma de percorrer a tupla com o for (somente dados)
for comida in lanche:
    print(f"Eu vou comer {comida}.")
print("Comi muito!")

# 2ª forma de percorrer a tupla com o for (dados + posição)
for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}.")
print("Comi muito!")

# 3ª forma de percorrer a tupla com o for (dados + posição)
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}.")




