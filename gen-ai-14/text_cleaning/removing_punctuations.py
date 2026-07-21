# 3. REMOVE PUNCTUATIONS
# usual python
import string
text = "Hello!!! I have 2 cats."
cleaned = text.translate(str.maketrans('', '', string.punctuation))
print(cleaned)  
# Output: Hello I have 2 cats

# using regex
import re
text = "Hello!!! I have 2 cats."
cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(cleaned)  
# Output: Hello I have 2 cats