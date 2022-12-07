import re

text = "To be, or not to be, that is the question"
vowels = re.findall("a|e|i|o|u", text)
print(len(vowels))