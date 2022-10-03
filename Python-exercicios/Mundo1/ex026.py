# PROGRAMA PARA INDICAR A PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING
frase = str(input("Digite uma frase: ")).strip()
print("A letra A apareceu {} vezes na frase" .format(frase.lower().count("a")))
print("A letra A apareceu a primeira vez na posição {}".format(frase.lower().find("a")+1))
# Find anterior(find) da esquerda para a direita(ordem direta)
print("A última letra A apareceu na posição {}" .format(frase.lower().rfind("a")+1))
# Find anterior (rfind) da direita para a esquerda(de trás para frente)
