# 6. Crie uma lista com as palavras de uma string que tenham mais de 3 letras.

frase = "Três pratos de trigo para três tigres tristes"
palavras_maiores_3 = [palavra for palavra in frase.split() if len(palavra) > 3]
print(palavras_maiores_3)

# Um passa tempo

frase_usuario = input("Digite uma frase: ")
palavras_maiores_3_usuario = [palavra for palavra in frase_usuario.split() if len(palavra) > 3]
print("Palavras com mais de 3 letras na frase:", palavras_maiores_3_usuario)