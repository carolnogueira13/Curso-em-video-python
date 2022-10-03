nome = str(input("Qual é o seu nome? "))
if nome == "Ana Caroline":
    print("O seu nome é bonito!")
elif nome == "José" or nome == "Maria":
    print("O seu nome é comum no Brasil.")
elif nome in "Gabriela Fernanda Juliana":
    print("Seu nome é um nome feminino bonito.")
else:
    print("Seu nome é comum!")
print(f"Prazer em te conhecer,{nome}")
