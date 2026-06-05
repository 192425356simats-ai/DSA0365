words = ["running", "playing", "studies", "flies"]
for word in words:
    if word.endswith("ing"):
        stem = word[:-3]
    elif word.endswith("es"):
        stem = word[:-2]
    elif word.endswith("s"):
        stem = word[:-1]
    else:
        stem = word
    print(word, "->", stem)
