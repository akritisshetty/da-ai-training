#using nltk word_tokenization()

import nltk
from nltk.tokenize  import word_tokenize
#nltk.download('punkt')
#nltk.download('punkt_tab)

text = "wow!! 😁 I bought smartphone for ₹29,999, and it's amazing!📱 The battery lasts only 6hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer"
print(word_tokenize(text))