# 3. Crie uma lista com as letras maiúsculas de uma string qualquer.

letra_maiuscula = [letra for letra in "Exemplo de String" if letra.isupper()]
print(letra_maiuscula)

# Um passa tempo

palavra = input("Digite uma palavra: ")
letras_maiusculas = [letra for letra in palavra if letra.isupper()]
print("Letras maiúsculas na palavra:", letras_maiusculas)