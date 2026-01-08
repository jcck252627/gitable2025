import random
import art

EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5
turns = 0

def pick_number():
    print(art.logo)
    print("Welcome to the Number Guess Game !!!")
    return random.randint(1,100)

def compare(picked, guessed, turns):
    """
    compare the two numbers, the cpu picked one and the user guessed one and determine if it's the right answer if not deduct
    one turn from the available turns
    """
    if picked == guessed:
        print(f"You hit the number !! {picked} is it !!")
        print(f"The number player picked is {guessed}  VS. number computer picked {picked}")
        print(art.game_over_win)
        return turns
    elif picked > guessed:
        print(f"{guessed} is Too low !! ... please guess again")
        return turns-1
    else:
        print(f"{guessed} is Too high !! ... please guess again")
        return turns-1

def set_diffculty():
    while True:
        game_mode = input(
                "Please enter 'easy' or 'hard' mode ... hard mode you get 5 guesses, while easy mode you have 10 tries:  ").lower()

        if game_mode =="easy":
                return EASY_MODE_TURNS
        elif game_mode =="hard":
                return HARD_MODE_TURNS
        else:
                print("please enter only the word 'easy or 'hard'  ........")

def gameflow():
    print(".......................................")
    number_picked= pick_number()
    # print(f"The number picked by computer is:  {number_picked}")


    # while turn != 100:
    turns = set_diffculty()
    print(f"You have {turns} attempts remaining to guess the number")
    number_guessed = 0
    while number_guessed != number_picked and turns > 0:
        while True:
            try:
                number_guessed=int(input("Pick a number between 1 and 100 you want to guess:  "))
                if 1 <= number_guessed <=100:
                    break
                else:
                    print("Please enter a number that is between ***1 and 100*** !!")
            except ValueError:
                    print("Invalid input, please enter an INTEGER number ....")


        turns = compare(number_picked, number_guessed, turns)
        print(f"You have {turns} attempts left to guess")
        if turns == 0:
            print("You have ran out of all your chances to guess ...........")
            print(art.game_over_lost)



gameflow()