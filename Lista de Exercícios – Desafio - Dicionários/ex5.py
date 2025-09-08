# 5. Dicionário Circular Crie um dicionário em que a última chave aponte para a primeira chave.

def create_circular_dict(keys, value):
    if not keys:
        return value
    circular_dict = {}
    current = circular_dict
    for key in keys[:-1]:
        current[key] = {}
        current = current[key]
    current[keys[-1]] = circular_dict  
    return circular_dict
keys = ['a', 'b', 'c']
value = 100
circular_dict = create_circular_dict(keys, value)
print("Dicionário circular:", circular_dict)
keys = ['x', 'y', 'z']
value = 42
circular_dict = create_circular_dict(keys, value)
print("Dicionário circular:", circular_dict)