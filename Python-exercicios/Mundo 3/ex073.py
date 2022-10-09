# PROGRAMA COLOCAÇÃO DE TIMES DE FUTEBOL
lista = ("Palmeiras", "Corinthians", "Internacional", "Flamengo", "Fluminense", "Atlético-PR",
         "Atlético-MG", "América-MG", "Botafogo", "São Paulo", "Fortaleza", "Bragantino", "Goiás", "Santos",
         "Ceará", "Coritiba", "Cuiabá", "Atlético-GO", "Avaí", "Juventude")
print("-"*100)
print(f"Lista de times do Brasileirão: {lista}")
print("-"*100)
print(f"Os cinco primeiros são: {lista[:5]}")
print("-"*100)
print(f"Os quatro últimos são: {lista[-4:]}")
print("-"*100)
print(f"Times em ordem alfabética: {sorted(lista)}")
print("-"*100)
print(f"O time Botafogo está na {lista.index('Botafogo') + 1}ª posição.")