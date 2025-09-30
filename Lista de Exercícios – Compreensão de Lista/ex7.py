# 7. Crie uma lista com os números primos de 1 a 20. Dica: use uma função para verificar se o número é primo ou não.

lista = [
    num for num in range(1, 21)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num != 1
]
print(lista)