# 2. REMOVING NUMBERS
# usual python
text = "Hello I have 2 cats and 3 dogs."
cleaned = ''.join([i for i in text if not i.isdigit()])
print(cleaned)
# Output: Hello I have  cats and  dogs

# using regex
import re
text = "Hello I have 2 cats and 3 dogs."
cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
print(cleaned)
# Output: Hello I have  cats and  dogs