# 10. Crie um programa que leia o conteúdo do arquivo "numeros.txt" (contendo
# números inteiros separados por vírgula), some esses números e exiba o
# resultado.

arquivo = open("numeros.txt", "r")
conteudo = arquivo.read()
numeros = map(int, conteudo.split(","))
soma = sum(numeros)
print(f"A soma dos números no arquivo 'numeros.txt' é {soma}.")
arquivo.close()