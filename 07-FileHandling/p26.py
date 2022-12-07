import re

text = "To be, or not to be, that is the question"
words = re.findall(r'\b\w+\b', text)
print(len(words))