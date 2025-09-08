# 3. Crie um programa que conte e exiba o número de linhas no arquivo "texto.txt".

arquivo = open("texto.txt", "r")
linhas = arquivo.readlines()
print(f"O arquivo 'texto.txt' tem {len(linhas)} linhas.")
arquivo.close()