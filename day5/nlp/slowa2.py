import ssl

from gensim.models import Word2Vec
import nltk

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('punkt')
nltk.download('punkt_tab')
from nltk import word_tokenize

# [nltk_data] Downloading package punkt to
# [nltk_data]     /Users/radoslawjaniak/nltk_data...
# [nltk_data]   Package punkt is already up-to-date!
# [nltk_data] Downloading package punkt_tab to
# [nltk_data]     /Users/radoslawjaniak/nltk_data...
# [nltk_data]   Package punkt_tab is already up-to-date!

# Przykładowy korpus – lista zdań
corpus = [
    "Król rządził swoim królestwem.",
    "Królowa była bardzo mądra.",
    "Książka leżała na stole.",
    "Pies biegał w ogrodzie.",
    "Kot siedział na płocie.",
    "Samochód jechał po drodze.",
    "Telefon dzwonił cały czas.",
    "Komputer pracował bez zarzutu.",
    "Drzewo rosło w parku.",
    "Dom był bardzo duży."
]

# tokenizacja
tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]

# Trening modelu
model = Word2Vec(sentences=tokenized_corpus, vector_size=50, window=5, min_count=1, workers=4)

# przykładowa wektoryzacja
vector_krol = model.wv['król']
vector_krolowa = model.wv['królowa']

print("Wektor dla 'król':")
print(vector_krol)
print("\nWektor dla 'królowa':")
print(vector_krolowa)

# podobienstwo kosinusowe
similarity = model.wv.similarity("król", "królowa")
print(f"Podobieństwo kosinusowe pomiędzy 'król' i 'królowa: {similarity:.4f}")
# Podobieństwo kosinusowe pomiędzy 'król' i 'królowa: 0.0906

# znalezienie słó∑ najbardziej podobnych do "król"
similar_words = model.wv.most_similar("król", topn=5)
print("Najbardziej podobne słowa do król:")
for word, sim in similar_words:
    print(f"{word}: {sim:.4f}")
# Najbardziej podobne słowa do król:
# cały: 0.2399
# parku: 0.2398
# pies: 0.2364
# ogrodzie: 0.2240
# rosło: 0.2033
