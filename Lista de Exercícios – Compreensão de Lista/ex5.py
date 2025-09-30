# 5. Crie uma lista com os números divisíveis por 3 e 5 de 1 a 30.

num_div = [x for x in range(1, 31) if x % 3 == 0 and x % 5 == 0]
print(num_div)