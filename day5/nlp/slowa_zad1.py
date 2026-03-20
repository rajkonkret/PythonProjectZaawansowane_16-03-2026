import math

words = ["król", "królowa"]

vocab = sorted(set("".join(words)))
print(vocab)  # ['a', 'k', 'l', 'o', 'r', 'w', 'ó']


# wektoryzacja
def vectorize_word(word, vocab):
    vector = [0] * len(vocab)
    for letter in word:
        index = vocab.index(letter)
        vector[index] += 1

    return vector


# podobieństwo cosinusowe
def cosine_similiarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    else:
        return dot_product / (norm1 * norm2)


vec_krol = vectorize_word("król", vocab)
print(vec_krol)  # [0, 1, 1, 0, 1, 0, 1]
# 0.7559289460184544 - wyrazy bliskie sobie

vec_krolowa = vectorize_word("królowa", vocab)
print(vec_krolowa)  # [0, 1, 1, 0, 1, 0, 1]

similarity = cosine_similiarity(vec_krol, vec_krolowa)
print(similarity)
