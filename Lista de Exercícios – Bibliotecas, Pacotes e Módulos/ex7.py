# 7. Importe a biblioteca matplotlib e crie um gráfico de barras simples com alguns dados fictícios.

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 23, 7, 15, 30]

plt.bar(categorias, valores, color='skyblue')

plt.title('Gráfico de Barras Simples')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()