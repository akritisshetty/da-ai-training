from nltk.stem import SnowballStemmer
snow = SnowballStemmer('english')

words = ['running','lover','runner','studies','organization','intention','easily','fairly']
print("Snowball Stemmer results:")
for w in words:
    print(w, "->",snow.stem(w))