from nltk.stem import PorterStemmer
porter = PorterStemmer()

words=['running','happiness','runner','studies','organization','intention','easily','fairly']
print("Porter Stemmer results:")
for w in words:
    print(w, "->",porter.stem(w))