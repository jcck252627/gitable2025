import random
import nltk

# download once (quiet to avoid long output)
nltk.download("words", quiet=True)
from nltk.corpus import words


def get_random_word():
    word_list = words.words()
    valid_words = [w.lower() for w in word_list if len(w) in (5, 6)]
    return random.choice(valid_words)


# --- Hangman ASCII Art for each life state ---
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# --- Generate a small pool of unique random words ---
wordlist = list(set(get_random_word() for _ in range(20)))  # set removes duplicates
print("Generated words:", wordlist)

# --- Game setup ---
player_lives = 6
chosen_word = random.choice(wordlist)
print("The chosen word is:  " + chosen_word + "  ...GAME STARTED ... you starting out with 6 lives")

print(f"Guess a word that has {len(chosen_word)} letters .... your mission is to fill these blanks")
print("_ " * len(chosen_word))
print("********************************************")

game_end = False
correct_letters_keep = []
wrong_letters_keep = []

while not game_end:
    # show hangman and wrong guesses
    print(HANGMAN_PICS[6 - player_lives])
    print("Wrong guesses so far: ", " ".join(wrong_letters_keep))

    # get input and validate
    guess = input("Please type in your guess letter:  ").lower()
    while len(guess) != 1 or not guess.isalpha():
        print("you have entered incorrect input, try again .....")
        guess = input("Please type in your guess letter:  ").lower()

    print("______________________")

    # already guessed -> penalize and continue
    if guess in correct_letters_keep or guess in wrong_letters_keep:
        player_lives -= 1
        print(f"You already guessed '{guess}' before! You lose a life. Lives left: {player_lives}")
        if player_lives == 0:
            print(HANGMAN_PICS[6])
            print("Game is over.. You LOSE .... HANGMAN !!!!")
            break
        continue

    # check occurrences of the guessed letter
    hit = chosen_word.count(guess)

    if hit > 0:
        correct_letters_keep.append(guess)
        print(f"Great job! You found {hit} occurrence(s) of '{guess}' ...you still have {player_lives} lives remaining")
    else:
        wrong_letters_keep.append(guess)
        player_lives -= 1
        print(f"Oops! '{guess}' is not in the word.")
        print(f"You have {player_lives} live(s) left !!!!!!!!")
        print("-------------------------------------------------------------------")
        if player_lives == 0:
            print(HANGMAN_PICS[6])
            print("Game is over..You LOSE .... HANGMAN !!!! The word was:", chosen_word)
            game_end = True

    # build and show current display
    display = "".join([letter if letter in correct_letters_keep else "_" for letter in chosen_word])
    print("These are the blanks filled so far ....")
    print(" ".join(display))  # spacing for readability

    # win condition
    if "_" not in display:
        game_end = True
        print("🎉 You Win ! The word was:", chosen_word)