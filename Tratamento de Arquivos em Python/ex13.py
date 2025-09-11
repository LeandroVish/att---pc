# 13. Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado. 
# Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas. 
# Adicione na última linha de cada página o número da página
# atual e o nome do arquivo original.

arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")

with open(arquivo_entrada, "r") as entrada:
    linhas = entrada.readlines()
with open(arquivo_saida, "w") as saida:
    pagina = 1
    linha_atual = 0
    for linha in linhas:
        while len(linha) > 76:
            saida.write(linha[:76] + "\n")
            linha = linha[76:]
            linha_atual += 1
            if linha_atual == 60:
                saida.write(f"\nPágina {pagina} - {arquivo_entrada}\n\n")
                pagina += 1
                linha_atual = 0
        saida.write(linha)
        linha_atual += 1
        if linha_atual == 60:
            saida.write(f"\nPágina {pagina} - {arquivo_entrada}\n\n")
            pagina += 1
            linha_atual = 0
    if linha_atual > 0:
        saida.write(f"\nPágina {pagina} - {arquivo_entrada}\n")