# before running this program we have to download the en_core_web_sm model
# to download python -m spacy download en_core_web_sm

import spacy  # spacy is a fast and efficient python library
nlp = spacy.load("en_core_web_sm")  # spacy.load()loads the english language
# nlp is processing pipeline
doc = nlp("""Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing! 📱 The battery lasts only 6hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer """)
tokens = [token.text for token in doc]
# nlp() function tokenizes the text and creates a doc object
print(tokens)

# output: ['Wow', '!', '!', '🤩', 'I', 'bought', 'this', 'smartphone', 'for', '₹', '29,999', ',', 'and', 'it', "'s", 'amazing', '!', '📱', 'The', 'battery', 'lasts', 'only', '6hours', '.', '😕', 'Thanks', '@MobileHub', '!', 'Visit', 'https://www.mobilehub.com', '.', 'I', "'d", 'definitely', 'buy', 'again', '!', '#', 'HappyCustomer']