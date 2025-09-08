# 8. Crie um programa que adicione a frase "Isso é incrível!" ao final do arquivo "texto.txt".

arquivo = open("texto.txt", "a")
arquivo.write("\nIsso é incrível!")
arquivo.close()
print("Frase adicionada ao final do arquivo 'texto.txt' com sucesso.")