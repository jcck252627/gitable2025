import random

# nature language toolkit library
import nltk

#import from a static word library of words ... another list of words stored in file ... as a secondary source of words
from hangman_words_libs import hm_word_list_module
from hangman_art import stages   # getting the ascii art for stage of the game
from hangman_art import hangman_logo # getting the ascci art for tje beginning

# download once (quiet to avoid long output)
nltk.download("words", quiet=True)
from nltk.corpus import words

def get_random_word():
    word_list = words.words()
    valid_words = [w.lower() for w in word_list if len(w) in (5, 6)]
    return random.choice(valid_words)

# generate a small pool of words (change count as desired)
random_words_list = [get_random_word() for _ in range(7)]
print(random_words_list)
print("Generated words:", random_words_list,"  ...From the nltk library")

wordlist = random_words_list

# game setup
player_lives = 6
# print logo
# print(hangman_logo)
chosen_word = random.choice(wordlist)
chosen_word2 = random.choice(hm_word_list_module)
print("The primary chosen word is:  " + chosen_word + "  ...GAME STARTED ... you starting out with 6 lives")
print("The secondary chosen word (not used) is:  "+chosen_word2)

print(f"Guess a word that has {len(chosen_word)} letters .... your mission is to fill these blanks")
print("_ " * len(chosen_word))
print("********************************************")

game_end = False
correct_letters_keep = []

while not game_end:
    # get input and validate
    guess = input("Please type in your guess letter:  ").lower()
    while len(guess) != 1 or not guess.isalpha():
        print("you have entered incorrect input, try again .....")
        guess = input("Please type in your guess letter:  ").lower()

    print("______________________")

    # already guessed -> penalize and continue
    if guess in correct_letters_keep:
        player_lives -= 1
        print(f"You already guessed '{guess}' before! You lose a life. Lives left: {player_lives}")
        if player_lives == 0:
            print("Game is over.. You LOSE .... HANGMAN !!!!")
            break
        continue

    # check occurrences of the guessed letter
    hit = chosen_word.count(guess)

    if hit > 0:
        # correct guess: record it once and congratulate
        correct_letters_keep.append(guess)
        print(f"great job ...you still have {player_lives} live remaining")
    else:
        # wrong guess: deduct life
        player_lives -= 1
        print(f"You have {player_lives} live(s) left !!!!!!!!")
        print("-------------------------------------------------------------------")
        if player_lives == 0:
            print("Game is over..You LOSE .... HANGMAN !!!!")
            game_end = True

    # build and show current display
    display = "".join([letter if letter in correct_letters_keep else "_" for letter in chosen_word])
    print("These are the blanks filled so far ....")
    print(display)

    # win condition
    if "_" not in display:
        game_end = True
        print("You Win !")
