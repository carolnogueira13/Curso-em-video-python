# PROGRAMA ANALISANDO E GERANDO DICIONÁRIOS
def notas(*num, sit=False):
    """
    -- Função para analisar as notas e a situção do aluno
    :param num: Uma ou várias notas dos alunos
    :param sit: Opcional, indica se quer ou não saber a situação do aluno
    :return: Dicionário com as informações do aluno
    """
    aluno = dict()
    aluno["total"] = len(num)
    aluno["maior"] = max(num)
    aluno["menor"] = min(num)
    aluno["média"] = sum(num)/len(num)
    if sit:
        if aluno["média"] >= 7:
            aluno["situação"] = "BOA"
        elif aluno["média"] >= 5:
            aluno["situação"] = "RAZOÁVEL"
        else:
            aluno["situação"] = "RUIM"
    return aluno


# Programa principal:
resp = notas(9.5, 7, 10, sit=True)
print(resp)
help(notas)
