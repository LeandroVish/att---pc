# 9. Crie uma lista de strings com os primeiros 10 nomes da lista de nomes.

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana", "Karina", "Lucas"]
primeiros_nomes = [nomes[i] for i in range(10)]
print(primeiros_nomes)