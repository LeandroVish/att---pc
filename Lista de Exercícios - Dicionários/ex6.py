# 6. Crie uma função que retorne a quantidade de pessoas no dicionário.

pessoas = {}

pessoas["a"] = "Ana"
pessoas["b"] = "Bruno"
pessoas["c"] = "Carlos"
pessoas["d"] = "Daniela"
pessoas["e"] = "Eduardo"

def contar_pessoas():
    return len(pessoas)

# Teste
quantidade = contar_pessoas()
print(f"Quantidade de pessoas no dicionário: {quantidade}")