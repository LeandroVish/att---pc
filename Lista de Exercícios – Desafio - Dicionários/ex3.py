# 3. Palavras Únicas por Chave Dado um dicionário de listas, encontre as palavras que são únicas para cada chave.

data = {
    'frutas': ['maçã', 'banana', 'laranja'],
    'vegetais': ['cenoura', 'batata', 'maçã'],
    'grãos': ['arroz', 'feijão', 'milho', 'banana']
}
print("Dicionário de dados:", data)

def unique_words(data):
    all_words = {}
    for key, words in data.items():
        for word in words:
            if word not in all_words:
                all_words[word] = {key}
            else:
                all_words[word].add(key)
    
    unique = {key: [] for key in data.keys()}
    for word, keys in all_words.items():
        if len(keys) == 1:
            unique_key = list(keys)[0]
            unique[unique_key].append(word)
    
    return unique

resultado = unique_words(data)
print("Palavras únicas por chave:", resultado)