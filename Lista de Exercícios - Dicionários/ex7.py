# 7. Crie uma função que retorne a média das idades das pessoas no dicionário.

idades = {}

idades["Lucas"] = 25
idades["Maria"] = 30
idades["João"] = 22
idades["Ana"] = 28
idades["Pedro"] = 35

print("Idades:", idades)

def calcular_media_idades():
    if not idades:
        return 0
    total_idades = sum(idades.values())
    quantidade_pessoas = len(idades)
    media = total_idades / quantidade_pessoas
    return media

# Teste
media_idades = calcular_media_idades()
print(f"A média das idades é: {media_idades:.2f} anos.")