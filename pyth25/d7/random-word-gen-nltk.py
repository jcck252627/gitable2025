import random
import nltk

# Make sure you download the word list the first time
nltk.download("words")
from nltk.corpus import words

def get_random_word():
    # grab all words
    word_list = words.words()
    # filter only 5 or 6 letter words
    valid_words = [w.lower() for w in word_list if len(w) in [5, 6]]
    return random.choice(valid_words)

# Example usage - store the words in a list and print them

random_words_list =[]
for _ in range(10):
    random_words_list.append(get_random_word())
    print("here are the words list generated ....\n"+get_random_word())
    print(random_words_list)