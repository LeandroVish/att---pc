# 7. Frequência de Palavras em Texto
# Conte a frequência de cada palavra em um texto usando um dicionário.

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency
text = "Este é um texto de exemplo. Este texto é apenas um exemplo!"
freq = word_frequency(text)
print("Frequência de palavras:", freq)
text = "Outro exemplo de texto, com algumas palavras repetidas: texto, exemplo, palavras."
freq = word_frequency(text)
print("Frequência de palavras:", freq)