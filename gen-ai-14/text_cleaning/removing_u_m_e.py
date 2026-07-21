# 4. REMOVING URL, MAIL, MENTIONS, EMOJIS
import re
text = "Hello @user!!! Visit https://www.example.com or email me at user@gmail.com"
cleaned = re.sub(r'http\S+|www\S+|https\S+|@\S+|[^a-zA-Z\s]', '', text)
print(cleaned)
# Output: Hello  Visit  or email me at user