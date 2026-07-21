# 5. REMOVING STOP WORDS
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

words = ['i', 'absolutely', 'love', 'this', 'mobile', 'phone']
# print(words)
filtered = [word for word in words if word not in stopwords.words('english')]
print(filtered)

# Output: ['absolutely', 'love', 'mobile', 'phone']