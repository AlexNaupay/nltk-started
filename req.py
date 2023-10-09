import nltk
import re

f = open('../requerimiento-0069-2023-igp-gg-otidg.txt')
text = f.read()
# print(text)

text = re.sub(r'<.*?>', ' ', text)  # clean text: html tags
text = re.sub(r'\s+', ' ', text)  # text: more spaces
print(text)

words = nltk.word_tokenize(text, 'spanish')
# words = [word for word in words if len(word) > 1]

# Frequency
fd = nltk.probability.FreqDist(words)
print(fd.items())
# fd.tabulate()  # table
# fd.pprint()
print(fd.most_common(2))  # Most common
# fd.plot()  # A plot
# print(list(fd))


# Bigrams
bigrams = nltk.bigrams(words)
bigrams_list = list(bigrams)  # As python list
fd_bigrams = nltk.probability.FreqDist(bigrams_list)
# fd_bigrams.plot(5)
print(fd_bigrams.most_common(5))
print(bigrams_list)

# FILTERING WORDS
threshold = 3
filtered_bigrams = [bigram for bigram in bigrams_list if len(bigram[0]) > threshold and len(bigram[1]) > threshold]
filtered_dist = nltk.probability.FreqDist(filtered_bigrams)
print('-' * 25)
print('filtered bigram list')
print(filtered_bigrams[:10])
# filtered_dist.plot(15)

# COLLOCATIONS
# ver documentación https://www.nltk.org/_modules/nltk/metrics/association.html
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(words)

finder.apply_freq_filter(3)
print(finder.nbest(bigram_measures.pmi, 10))
