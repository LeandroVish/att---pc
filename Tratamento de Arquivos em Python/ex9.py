# 9. Crie um programa que leia o conteúdo do arquivo "texto.txt" e conte quantas
# letras (excluindo espaços) estão presentes no texto.

arquivo = open("texto.txt", "r")
conteudo = arquivo.read()
letras = len(conteudo.replace(" ", "").replace("\n", ""))
print(f"O arquivo 'texto.txt' tem {letras} letras (excluindo espaços).")
arquivo.close()