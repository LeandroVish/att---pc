# 10. Crie uma função que retorne uma lista com as pessoas cujo nome começa com a letra "J".

pessoas = {}

pessoas["a"] = "Ana"
pessoas["b"] = "Bruno"
pessoas["c"] = "João"
pessoas["d"] = "Daniela"
pessoas["e"] = "Júlia"

def nomes_com_j():
    lista_j = [nome for nome in pessoas.values() if nome.startswith("J")]
    return lista_j

# Teste
resultado = nomes_com_j()
print("Pessoas cujo nome começa com 'J':", resultado)