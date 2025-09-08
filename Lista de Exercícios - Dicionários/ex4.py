#4. Crie uma função que receba um nome e uma nova idade como parâmetros e atualize a idade da pessoa correspondente no dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

print(f"Idades do João antes da atualização: {idades['João']}")

def atualizar_idade(nome, nova_idade):
    if nome in idades:
        idades[nome] = nova_idade
        return f"Idade de {nome} atualizada para {nova_idade} anos."
    else:
        return "Nome não encontrado."

# Teste
nome_pesquisado = "João"
nova_idade = 23
resultado = atualizar_idade(nome_pesquisado, nova_idade)
print(resultado)

print(f"Idades do João após a atualização: {idades['João']}")