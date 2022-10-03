# PROGRAMA VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
cidade = str(input("Em que cidade você nasceu? ")).strip()  # strip para retirar os espaços que o usuário pode digitar
print("santo" in cidade[:5].lower())    # lower passa tudo para caixa baixa para conseguir identificar corretamente
