# 9. Crie uma função que retorne a pessoa mais nova do dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

print("Idades:", idades)

def pessoa_mais_nova():
    if not idades:
        return None, None
    nome_mais_novo = min(idades, key=idades.get)
    idade_mais_novo = idades[nome_mais_novo]
    return nome_mais_novo, idade_mais_novo

# Teste
nome, idade = pessoa_mais_nova()
if nome:
    print(f"A pessoa mais nova é {nome} com {idade} anos.")
else:
    print("O dicionário está vazio.")