# 8. Escreva um programa que importe o pacote matplotlib e plote a função seno.

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Função Seno')
plt.xlabel('x (radianos)')
plt.ylabel('sin(x)')
plt.grid()
plt.show()