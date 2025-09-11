# 14. Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre
# as palavras e o fim das linhas. O arquivo de saída também não deve ter mais de
# uma linha em branco repetida.

arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")
with open(arquivo_entrada, "r") as entrada:
    linhas = entrada.readlines()
with open(arquivo_saida, "w") as saida:
    linha_anterior_vazia = False
    for linha in linhas:
        linha = ' '.join(linha.split())
        if linha == '':
            if not linha_anterior_vazia:
                saida.write('\n')
                linha_anterior_vazia = True
        else:
            saida.write(linha + '\n')
            linha_anterior_vazia = False
print(f"Arquivo '{arquivo_saida}' criado com sucesso, eliminando espaços repetidos.")