# 4. Crie um programa que copie o conteúdo do arquivo "texto.txt" para um novo arquivo chamado "copia.txt".

texto = open("texto.txt", "r")
copia = open("copia.txt", "w")
for linha in texto.readlines():
    copia.write(linha)
texto.close()
copia.close()
print("Conteúdo copiado para 'copia.txt' com sucesso.")