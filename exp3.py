word = input("Enter a word: ")
if word.endswith("ing"):
    stem = word[:-3]
elif word.endswith("ed"):
    stem = word[:-2]
elif word.endswith("s"):
    stem = word[:-1]
else:
    stem = word
print("Original Word:", word)
print("Root Word:", stem)
