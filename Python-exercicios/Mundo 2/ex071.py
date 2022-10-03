# PROGRAMA SIMULADOR DE CAIXA ELETRÔNICO
print("-"*30)
print("BANCO AC")
print("-"*30)
valor = int(input("Qual valor você quer sacar? R$ "))

if valor >= 50:
    cedulasde50 = valor // 50
    valor = valor - (cedulasde50 * 50)
    print(f"Total de {cedulasde50} cédulas de R$ 50,00.")

if valor >= 20:
    cedulasde20 = valor // 20
    valor = valor - (cedulasde20 * 20)
    print(f"Total de {cedulasde20} cédulas de R$ 20,00.")

if valor >= 10:
    cedulasde10 = valor // 10
    valor = valor - (cedulasde10 * 10)
    print(f"Total de {cedulasde10} cédulas de R$ 10,00.")

if valor >= 1:
    cedulasde1 = valor // 1
    print(f"Total de {cedulasde1} cédulas de R$ 1,00.")

"""valor = int(input("Que valor você quer sacar? "))
total = valor
ced = 50
totaldecel = 0
while True:
    if total > ced:
        total -= ced
        totaldecel += 1
    else:
        if totaldecel > 0:
            print(f"Total de {totaldecel} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaldecel = 0
        if total = 0:
            break"""
