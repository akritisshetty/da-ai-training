from nltk.stem import LancasterStemmer
Lancaster = LancasterStemmer()

words = ['running','lover','runner','studies','organization','intention','easily','fairly']
print("Lancaster Stemmer results:")
for w in words:
    print(w, "->", Lancaster.stem(w))