import nltk
from nltk.corpus import wordnet

# nltk.download('omw-1.4')

# synset: grupo de sinómimos de una palabra.
ss = wordnet.synsets('carro', lang='spa')
print(wordnet.langs())  # languages keys
print(ss)

# explorando los synsets
for syn in ss:  # Syn: one by one
    print('Examples: ', syn.examples())
    print(syn.name(), ': ', syn.definition())  # definition
    for name in syn.lemma_names():  # Other words in the syn (synset)
        print('  -', name)


import networkx as nx
import matplotlib.pyplot as plt


def closure_graph(synset, fn, depth=7):
    seen = set()
    graph = nx.DiGraph()
    labels = {}

    def recurse(s):
        if not s in seen:
            seen.add(s)
            labels[s.name] = s.name().split('.')[0]
            graph.add_node(s.name)
            for s1 in fn(s)[:depth]:
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)

    recurse(synset)
    return graph, labels


def draw_text_graph(G, labels):
    plt.figure(figsize=(18, 12))
    pos = nx.planar_layout(G, scale=18)
    nx.draw_networkx_nodes(G, pos, node_color="red", linewidths=0, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=20, labels=labels)
    nx.draw_networkx_edges(G, pos)
    plt.xticks([])
    plt.yticks([])


# Hyponyms (more specific)
print('--- Hyponyms and Hypernyms ---')
print(ss[0].name())
print(ss[0].hyponyms())
# G, labels = closure_graph(ss[0], fn=lambda s: s.hyponyms())
# draw_text_graph(G, labels)

print(ss[0].name())
G, labels = closure_graph(ss[0], fn=lambda s: s.hypernyms())
draw_text_graph(G, labels)


## Similitud Semántica
def show_syns(word):
    ss = wordnet.synsets(word, lang='spa')
    for syn in ss:
        print(syn.name(), ': ', syn.definition())
        for name in syn.lemma_names():
            print('  -', name)
    return ss


ss1 = show_syns('perro')
ss2 = show_syns('gato')
ss3 = show_syns('animal')

print(ss1)
print(ss2)
print(ss3)

perro = ss1[0]
gato = ss2[0]
animal = ss3[0]

# similitud entre 'animal' y 'perro'
s1 = animal.path_similarity(perro)
s2 = gato.path_similarity(perro)
s3 = perro.path_similarity(perro)  # ->1 (more similar)

print(s1)
print(s2)
print(s3)

