# PROGRAMA CADASTRO DE TRABALHADOR DE PYTHON
from datetime import date

trabalhador = dict()
trabalhador['nome'] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
trabalhador['idade'] = date.today().year - ano # ou datetime.now().year
trabalhador['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input("Ano de contratação: "))
    trabalhador['salário'] = float(input("Salário: R$ "))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] + 35) - ano # Considerando a aposentadoria com 35 anos de contribuiçao

print("-"*50)
for k, v in trabalhador.items():
    print(f"- {k} tem o valor {v}")
