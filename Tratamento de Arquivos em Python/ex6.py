# 6. Crie um programa que conte e exiba o número de palavras no arquivo "texto.txt".

arquivo = open("texto.txt", "r")
conteudo = arquivo.read()
palavras = conteudo.split()
print(f"O arquivo 'texto.txt' tem {len(palavras)} palavras.")
arquivo.close()