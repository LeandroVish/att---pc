# 9. Dicionário de Matrizes
# Crie um dicionário de matrizes, onde as chaves são coordenadas e os valores são
# os elementos correspondentes.

def create_matrix_dict(rows, cols):
    matrix_dict = {}
    for i in range(rows):
        for j in range(cols):
            matrix_dict[(i, j)] = i * cols + j
    return matrix_dict

rows = 3
cols = 4
matrix_dict = create_matrix_dict(rows, cols)
print("Dicionário de matrizes:")
for key, value in matrix_dict.items():
    print(f"Coordenada {key}: Valor {value}")