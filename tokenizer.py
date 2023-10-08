import nltk
import re

nltk.download('cess_esp')

corpus = nltk.corpus.cess_esp.sents()
print(corpus)

texto = """ Cuando sea el rey del mundo  (imaginaba él en su cabeza) no tendré que  preocuparme por estas bobadas. 
            Era solo un niño de 7 años, pero pensaba que podría ser cualquier cosa que su imaginación le permitiera visualizar en su cabeza ..."""
print(texto)

pattern3 = r'[ \W\t\n]+'

print(re.split(pattern3, texto))

texto = 'En los E.U. esa postal vale $15.50 ...'
print(re.split(pattern3, texto))

pattern = r'''(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+         # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*       # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
              | \.\.\.             # ellipsis
              | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''

tokens0 = re.split(pattern, texto)
tokens = nltk.regexp_tokenize(texto, pattern)

print('-'*30)
print(tokens0)
print(tokens)
# nltk.word_tokenize(texto)
