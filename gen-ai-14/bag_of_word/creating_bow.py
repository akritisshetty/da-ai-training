from sklearn.feature_extraction.text import CountVectorizer
sentences = [
    "The cake was delicious and fresh",
    "The bread was fresh and soft",
    "Fresh cake and bread every day"
]
vectorizer = CountVectorizer()
# create a CountVectorizer object
# it will convert text into numbers by counting word occurrencces.
x = vectorizer.fit_transform(sentences)
print(x)
print(vectorizer.get_feature_names_out())
print(x.toarray())