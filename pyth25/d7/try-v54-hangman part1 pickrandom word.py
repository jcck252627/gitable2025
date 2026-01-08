import random

wordlist =["aardvark" ,"baboon" ,"camel"]

# pick random word from the existing word list
chosen_word = random.choice(wordlist)
print("The chosen word is:  "+chosen_word)

# ask user to guess a letter make guess lower case
guess = input("Please type in your guess letter:  ").lower()

while len(guess) !=1 or not guess.isalpha():
    print("you have entered incorrect input, try again .....")
    guess = input("Please type in your guess letter:  ").lower()
print(guess)
print("______________________")


# check this letter against the word picked in chosen word
hit =0
for letter in chosen_word:
    if letter == guess:
        print("You have pick a right letter !!!")
        print ("your guess of "+guess +" matches "+letter +" in the word "+chosen_word )
        hit += 1
        print(f"You hit the correct letter {hit} time(s)")

