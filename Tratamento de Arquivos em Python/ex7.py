# 7. Crie um programa que leia o conteúdo do arquivo "texto.txt" e substitua
# todas as ocorrências da palavra "mundo" por "Python". O novo conteúdo deve ser
# escrito em um novo arquivo chamado "modificado.txt".

arquivo = open("texto.txt", "r")
novo_arquivo = open("modificado.txt", "w")
for linha in arquivo.readlines():
    for letra in linha:
        if letra in "mundo":
            novo_arquivo.write("Python")
        else:
            novo_arquivo.write(letra)
arquivo.close()
novo_arquivo.close()
print("Conteúdo modificado escrito em 'modificado.txt' com sucesso.")