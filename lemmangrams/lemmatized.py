from pymystem3 import Mystem
mystem = Mystem()

with open('karenina.txt', 'r') as text:
    text = text.read()

lemmas = mystem.lemmatize(text)
lemmas = ''.join(lemmas)
lemmas = lemmas.lower()

with open('lemmatized.txt', 'w', encoding='utf8') as outputFile:
    outputFile.write(lemmas)
print('Done!')