import random
from english_words import get_english_words_set
# pip install english-words

def get_random_english_word():
    # Get a set of English words: lowercase, alphabet-only
    words = get_english_words_set(sources=['web2'], lower=True, alpha=True)
    # Filter for words of length 5 or 6
    valid = [w for w in words if len(w) in (5, 6)]
    return random.choice(valid) if valid else None

# Example usage
for n in range (0,10):
    print(get_random_english_word())
