import random

def hard_word(min_length=8, filename="words.txt"):
    with open(filename) as wordbook:
        large_words = [line for line in wordbook if len(line) >= min_length]
    if large_words:
        return random.choice(large_words).rstrip('\n')
    else:
        print("No word found with at least %s characters.")

hard_words = []
hard_words = (hard_word(8))
print(hard_words)