# Simple FSM for generating plural nouns
def pluralize(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + "es"
    else:
        return noun + "s"
words = ["cat", "bus", "box", "dish"]
for word in words:
    print(word, "->", pluralize(word))
