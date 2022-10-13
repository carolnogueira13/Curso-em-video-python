# PROGRAMA PARA CONTAR VOGAIS EM UMA TUPLA
palavras = ("aprender",
            "programar",
            "linguagem",
            "python",
            "curso",
            "gratis",
            "estudar",
            "praticar",
            "trabalhar",
            "mercado",
            "programador",
            "futuro")

for cont in palavras:
    print(f"\nNa palavra aprender {cont.upper()} temos", end=" ")
    for vogal in cont:
        if vogal in "aeiou":
            print(vogal, end=' ')

