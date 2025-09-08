# 4. Aninhamento de Chaves Crie um dicionário aninhado com níveis de chaves fornecidos em uma lista.

def create_nested_dict(keys, value):
    if not keys:
        return value
    return {keys[0]: create_nested_dict(keys[1:], value)}

keys = ['a', 'b', 'c']
value = 100
nested_dict = create_nested_dict(keys, value)
print("Dicionário aninhado:", nested_dict)

keys = ['x', 'y', 'z']
value = 42
nested_dict = create_nested_dict(keys, value)
print("Dicionário aninhado:", nested_dict)