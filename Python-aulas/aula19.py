pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro'  # Troca a key 'nome' por 'Leandro'
pessoas['peso'] = 98.5  # Adicionando o item 'peso': 98.5 no dicionário
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f"{k} = {v}")
