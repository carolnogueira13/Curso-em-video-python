#PROGRAMA BOLETIM COM LISTAS COMPOSTAS
aluno = []
turma = []
while True:
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 01: ")))
    aluno.append(float(input("Nota 02: ")))
    turma.append(aluno[:])
    aluno.clear()
    resp = str(input("Quer continuar? [S/N] ")).upper()
    if resp == "N":
        break
print(turma)
print("-"*50)
print(f"{'No.':<4}{'NOME':<10}{'MÈDIA':>8}")
print("-"*30)
for pos, aluno in enumerate(turma):
    print(f"{pos:<4}{aluno[0]:<10}{((aluno[1]+aluno[2])/2):8.1f}")
print()
while True:
    resp = int(input("Mostrar as notas de qual aluno? (999 interrompe) "))
    if resp == 999:
        print("FINALIZANDO...")
        break
    elif resp <= len(turma)-1:
        print(f"Notas de {turma[resp][0]} são {turma[resp][1:]}")
    else:
        print("Aluno não encontrado! Tente novamente um número válido")
    print("-"*50)
print("VOLTE SEMPRE!")
