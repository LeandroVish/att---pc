#3. Crie uma função que receba um nome como parâmetro e retorne a idade da pessoa correspondente no dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

def obter_idade(nome):
    return idades.get(nome, "Nome não encontrado.")

# Teste
nome_pesquisado = "Maria"
idade = obter_idade(nome_pesquisado)
print(f"A idade de {nome_pesquisado} é: {idade}")

# Erro
nome_pesquisado = "Carlos"
idade = obter_idade(nome_pesquisado)
print(f"A idade de {nome_pesquisado} é: {idade}")