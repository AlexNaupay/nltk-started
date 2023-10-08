import nltk

nltk.download('cess_esp')

# Derivación simple
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
languages = SnowballStemmer.languages

print(languages)

stem = SnowballStemmer('spanish')
root = stem.stem('trabajando')
print(root)


# Lematización
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()
result = lemm.lemmatize('trabajando')
print(result)