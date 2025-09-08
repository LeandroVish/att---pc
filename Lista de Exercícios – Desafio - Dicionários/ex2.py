# 2. Maior Valor em Dicionário de Dicionários Encontre a chave e valor com o maior valor em um dicionário de dicionários.

data = {
    'item1': {'value': 10},
    'item2': {'value': 25},
    'item3': {'value': 15}
}

print("Dicionário de dados:", data)

def find_max_value(data):
    max_key = None
    max_value = float('-inf')  
    for key, sub_dict in data.items():
        if sub_dict['value'] > max_value:
            max_value = sub_dict['value']
            max_key = key
    return max_key, max_value
key, value = find_max_value(data)
print(f"Chave com maior valor: {key}, Valor: {value}")