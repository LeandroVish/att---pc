# 2. Crie um programa que leia o conteúdo do arquivo "texto.txt" criado no
# exercício anterior e o exiba no console.

texto = open("texto.txt", "r")
conteudo = texto.read()
print(conteudo)
texto.close()