#5. Crie uma função que remova uma pessoa do dicionário.

pessoas = {}

pessoas["a"] = "Ana"
pessoas["b"] = "Bruno"
pessoas["c"] = "Carlos"
pessoas["d"] = "Daniela"
pessoas["e"] = "Eduardo"

print(pessoas)

def remover_pessoa(chave):
    if chave in pessoas:
        del pessoas[chave]
        return f"Pessoa com a chave '{chave}' removida."
    else:
        return "Chave não encontrada."

# Teste
chave_para_remover = "c"
resultado = remover_pessoa(chave_para_remover)
print(resultado)
print(pessoas)