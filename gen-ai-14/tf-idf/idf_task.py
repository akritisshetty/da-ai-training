from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    "The cake was delicious and fresh",
    "The bread was fresh and soft",
    "Fresh cake and bread every day"
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
print("TF-IDF values:")
print(tfidf_matrix)
print("\n TF-IDF values in matrix form:")
print(tfidf_matrix.toarray())

print("\n IDF values:")
for ele1, ele2 in zip(vectorizer.get_feature_names_out(), vectorizer.idf_):
    print(ele1, ':', ele2)
print("\n vocabulary indexes:")
print(vectorizer.vocabulary_)