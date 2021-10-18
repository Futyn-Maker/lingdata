import re
from nltk.util import ngrams
import csv

n = int(input('Введите количество слов в n-граммах (то есть n):'))
with open('lemmatized.txt', 'r', encoding='utf8') as lemmas:
    text = lemmas.read()
text = re.sub(r'[^.!?\w\s]', '', text)

tokens = [token for token in text.split() if token != '']
ngrams = list(ngrams(tokens, n))
ngrams = [' '.join(ngram) for ngram in ngrams]

i = 0
while i <= len(ngrams) - 1:
    if re.search(r'\.|\!|\?', ngrams[i]) != None and ngrams[i][-1] != '.' and ngrams[i][-1] != '!' and ngrams[i][-1] != '?':
        ngrams.pop(i)
    ngrams[i] = re.sub(r'[.!?]', '', ngrams[i])
    i += 1

ngramList = {}

for ngram in ngrams:
    if ngram in ngramList:
        value = ngramList[ngram]
        ngramList[ngram] = value + 1
    else:
        ngramList[ngram] = 1

genQuantaty = sum(ngramList.values())

ngramArraySorted = sorted(ngramList, key=lambda x: int(ngramList[x]), reverse=True)
ngramTable = [['Ngram', 'Quantaty', 'Percent']]

for ngram in ngramArraySorted:
    ngramTable.append([ngram, ngramList[ngram], int((ngramList[ngram] * (100 / genQuantaty)) * 100)])

with open('ngrams.csv', 'w', encoding='utf8', newline='') as outFile:
    writer = csv.writer(outFile, delimiter=';')
    writer.writerows(ngramTable)
print('Done!')