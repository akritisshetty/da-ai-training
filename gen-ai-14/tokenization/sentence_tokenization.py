import nltk
from nltk.tokenize import sent_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")

text = """Artificial Intelligence is transforming industries. It helps automate repetitive tasks.Are you excited to learn NLP? Let's get started!"""
print(sent_tokenize(text))

# Output: ['Artificial Intelligence is transforming industries.', 'It helps automate repetitive tasks.Are you excited to learn NLP?', "Let's get started!"]