# 1. Mesclar Dicionários Combine dois dicionários, substituindo valores comuns pela soma dos valores correspondentes.

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

print("Dicionário 1:", dict1)
print("Dicionário 2:", dict2)

def merge_dicts(d1, d2):
    merged = d1.copy()  
    for key, value in d2.items():
        if key in merged:
            merged[key] += value  
        else:
            merged[key] = value  
    return merged

resultado = merge_dicts(dict1, dict2)
print("Dicionário mesclado:", resultado)