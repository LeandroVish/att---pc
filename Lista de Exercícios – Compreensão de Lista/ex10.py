# 10. Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de  nomes, mas com as primeiras letras maiúsculas.

nomes = ["ana", "bruno", "carla", "daniel", "eduardo", "fernanda", "gabriel", "helena", "igor", "juliana", "karina", "lucas"]
nomes_maiusculos = [nome.capitalize() for nome in nomes[:10]]
print(nomes_maiusculos)