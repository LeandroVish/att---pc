# 11. Crie uma lista de strings com os nomes dos primeiros 10 nomes da lista de nomes, mas sem as vogais.

nomes = ["ana", "bruno", "carla", "daniel", "eduardo", "fernanda", "gabriel", "helena", "igor", "juliana", "karina", "lucas"]
vogais = "aeiou"
nomes_sem_vogais = [''.join([letra for letra in nome if letra not in vogais]) for nome in nomes[:10]]
print(nomes_sem_vogais)