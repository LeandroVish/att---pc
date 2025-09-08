#2. Imprima o nome e a idade de todas as pessoas no dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

# Teste
for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos.")