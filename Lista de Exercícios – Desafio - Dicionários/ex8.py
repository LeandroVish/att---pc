# 8. Ordenação de Dicionário por Valor
# Ordene um dicionário com base nos valores, em ordem decrescente.

def sort_dict_by_value(data):
    return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

data = {
    'a': 10,
    'b': 5,
    'c': 15,
    'd': 3,
    'e': 20
}
sorted_dict = sort_dict_by_value(data)
print("Dicionário original:", data)
print("Dicionário ordenado por valor (decrescente):", sorted_dict)