# 2. Crie uma lista com os números ímpares de 1 a 50.

impares = [x for x in range(1, 51) if x % 2 != 0]
print(impares)