# 13. Criar um dicionário a partir de duas listas

chaves = ['nome', 'idade', 'cidade']
valores = ['Alice', 30, 'São Paulo']

dicionario = {chaves[i]: valores[i] for i in range(len(chaves))}
print(dicionario)