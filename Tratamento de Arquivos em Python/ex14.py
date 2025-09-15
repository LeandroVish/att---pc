# 14. Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre
# as palavras e o fim das linhas. O arquivo de saída também não deve ter mais de
# uma linha em branco repetida.

arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
arquivo_saida = input("Digite o nome do arquivo de saída: ")
with open(arquivo_entrada, "r") as entrada:
    linhas = entrada.readlines()
with open(arquivo_saida, "w") as saida:
    resultado = ''.join(linha.strip().replace(" ", "") for linha in linhas if linha.strip() != '')
    saida.write(resultado)
print(f"Arquivo '{arquivo_saida}' criado com sucesso, eliminando espaços repetidos.")