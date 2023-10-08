import nltk
from nltk.corpus import stopwords


def stopwords_percentage(text):
    """
    aqui usamos un recurso léxico (stopwords) para filtrar un corpus
    """
    stopwd = stopwords.words('spanish')
    stopwords_es = [w for w in text if w.lower() in stopwd]  # No stopwords
    return len(stopwords_es) / len(text)


f = open('../requerimiento-0069-2023-igp-gg-otidg.txt')
req_text = f.read()
# words = nltk.word_tokenize(req_text, 'spanish')
# words = [word for word in req_text if len(word) > 1]

stopwords_es = stopwords.words('spanish')  # stop words
print(stopwords_es)
print(len(stopwords_es))

words = nltk.word_tokenize(req_text)
print(len(words))

print('>>> Without stop words')
without_stop_words = [word for word in words if word.lower() not in stopwords_es]
print(without_stop_words)
print(len(without_stop_words))
print(f"Percentage of stop words: {stopwords_percentage(words)*100}")

# -----------
# translate
from nltk.corpus import swadesh
print(swadesh.fileids())  # Available languages

print(swadesh.words('en'))  # Available words in english

entries = swadesh.entries(['en', 'es'])  # From list of languages ['en', 'es', 'fr']
print(entries)
translator = dict(entries)  # As python dict
print(translator)
print(translator['swim'])
