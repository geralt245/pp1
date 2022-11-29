import re

with open("song.txt", "r") as f:
    content = f.read()
    words = re.findall(r"\b\S{6,}\b", content)
    print(words)