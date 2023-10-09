import nltk
from nltk.book import *

nltk.download('book')

# bigrams_ = bigrams(text1)

my_text = 'Alex is a superman superman'
my_tokens = nltk.word_tokenize(my_text,'english')
my_fd = nltk.probability.FreqDist(my_tokens)
print(my_fd.items())
my_fd.tabulate()  # table
my_fd.pprint()
print(my_fd.most_common(2))  # Most common
# my_fd.plot()  # A plot
# print(list(my_fd))

# BIGRAMS
md_bigrams = list(bigrams(text1))  # bigrams, then as list
print(md_bigrams[:10])

fdist = FreqDist(md_bigrams)  # Frequency distribution
# fdist.plot(15)

# FILTERING WORDS
threshold = 3
filtered_bigrams = [bigram for bigram in md_bigrams if (len(bigram[0]) > threshold and len(bigram[1]) > threshold)]
filtered_dist = FreqDist(filtered_bigrams)
filtered_dist.plot(15)

