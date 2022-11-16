# PROGRAMA FUNÇÕES PARA VOTAÇÃO
def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA!"
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL!"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO!"


ano = int(input("Ano de nascimento: "))
print(voto(ano))
