# 4. Crie uma lista com o comprimento de cada palavra em uma string.

frase = "Eu não gosto de ser contrariado"
tamanhos_palavras = [len(palavra) for palavra in frase.split()]
print(tamanhos_palavras)

# Um passa tempo

frase_usuario = input("Digite uma frase: ")
tamanhos_palavras_usuario = [len(palavra) for palavra in frase_usuario.split()]
print("Comprimento de cada palavra na frase:", tamanhos_palavras_usuario)