import random
import art

EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5

def pick_number():
    print(art.logo)
    print("Welcome to the Number Guess Game !!!")
    return random.randint(1,100)

def compare(picked, guessed):
    if picked == guessed:
        print(f"You hit the number !! {picked} is it !!")
    elif picked > guessed:
        print(f"{guessed} is Too low !!")
    else:
        print(f"{guessed} is Too high !!")

def set_diffculty():

    game_mode = input(
            "Please enter 'hard' or 'easy' mode ... hard mode you get 5 guesses, while easy mode you have 10 tries:").lower()

    if game_mode =="easy":
            return EASY_MODE_TURNS
    elif game_mode =="hard":
            return HARD_MODE_TURNS

print(".......................................")
number_picked= pick_number()
# print(f"The number picked by computer is:  {number_picked}")



turns = 0

# while turn != 100:
turns = set_diffculty()
print(f"You have {turns} attempts remaining to guess the number")

number_guessed = 0
while number_guessed != number_picked:
    number_guessed=int(input("Pick a number between 1 and 100 you want to guess:  "))
    print(f"The number player picked is {number_guessed}  VS. number computer picked {number_picked}")
    compare(number_picked, number_guessed)




# v92.....@@13:31 .... got code 57% working ...... 9/11
