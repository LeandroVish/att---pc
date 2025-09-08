# 8. Crie uma função que retorne a pessoa mais velha do dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

print("Idades:", idades)

def pessoa_mais_velha():
    if not idades:
        return None, None
    nome_mais_velho = max(idades, key=idades.get)
    idade_mais_velho = idades[nome_mais_velho]
    return nome_mais_velho, idade_mais_velho

# Teste
nome, idade = pessoa_mais_velha()
if nome:
    print(f"A pessoa mais velha é {nome} com {idade} anos.")
else:
    print("O dicionário está vazio.")