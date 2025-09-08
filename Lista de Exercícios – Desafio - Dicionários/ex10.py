# 10. Mapeamento de Palavras
# Crie um dicionário que mapeie palavras em um texto para palavras diferentes com
# base em um dicionário de substituição.

def map_words(text, mapping):
    words = text.split()
    mapped_words = [mapping.get(word, word) for word in words]
    return ' '.join(mapped_words)
text = "Eu odeio estudar no sabado"
mapping = {
    'odeio': 'adoro',
    'estudar': 'dormir',
    'no': 'em',
    'sabado': 'casa'
}
mapped_text = map_words(text, mapping)
print("Texto original:", text)
print("Texto mapeado:", mapped_text)