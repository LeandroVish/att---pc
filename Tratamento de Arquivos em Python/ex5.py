# 5. Crie um programa que leia o conteúdo dos arquivos "texto.txt" e
# "copia.txt", e escreva o conteúdo combinado em um terceiro arquivo
# chamado "combinado.txt".

arquivo1 = open("texto.txt", "r")
arquivo2 = open("copia.txt", "r")
combinado = open("combinado.txt", "w")
for linha in arquivo1.readlines():
    combinado.write(linha)
for linha in arquivo2.readlines():
    combinado.write(linha)
arquivo1.close()
arquivo2.close()
combinado.close()
print("Conteúdo combinado escrito em 'combinado.txt' com sucesso.")