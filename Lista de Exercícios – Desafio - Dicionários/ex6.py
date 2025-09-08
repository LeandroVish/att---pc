# 6. Compressão de Dicionário Comprima um dicionário removendo chaves com valores menores que um determinado limite.

def compress_dict(data, limit):
    return {k: v for k, v in data.items() if v >= limit}

data = {
    'a': 10,
    'b': 5,
    'c': 15,
    'd': 3,
    'e': 20
}
limit = 15
compressed = compress_dict(data, limit)
print("Dicionário original:", data)
print(f"Dicionário comprimido (limite={limit}):", compressed)