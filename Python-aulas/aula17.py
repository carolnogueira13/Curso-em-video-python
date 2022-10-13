num = [2, 3 ,9, 6]
print(num)
num[2] = 8
num.append(7) # Adiciona o elemento 7 no final da lista

num.sort() # Coloca os elementos da lista em ordem crescente

num.sort(reverse=True) # Coloca os elementos da lista em ordem decrescente

num.insert(2, 0) # A função insert insere o valor que vc quiser na posição que quiser, nesse caso o elemento 0 será
# inserido na posição 2 // nome_da_lista.insert(posição, elemento)

num.pop() # Eimina da lista o último elemento
num.pop(2) # Elimina o termo da posição 2

num.remove(9) # Elimina o elemento 9 na sua 1ª ocorrência

print(num)
print(f"Essa lista tem {len(num)} elementos")