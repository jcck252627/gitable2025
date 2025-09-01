import art
print(art.logo)

wordlist =["aardvark" ,"baboon" ,"camel"]

# pick random word from the existing word list

player_live = 6
chosen_word = random.choice(wordlist)
print("The chosen word is:  "+chosen_word)  #.... not printing the picked word

# print out the place holder blanks to be filled for user to visualize the mission .....
placeholder =""
letter_counts =0
for position in range(0, len(chosen_word)):
    placeholder += "_ "
    letter_counts += 1
    print("This is "+str(letter_counts)+" letter(s)")
print("Guess a word that has "+str(letter_counts)+" letters .... your mission is to fill these blinks")
print(placeholder)
print("********************************************")

game_end = False
correct_letters_keep =[]


while not game_end:
    # ask user to guess a letter and then make the input lower cased
    guess = input("Please type in your guess letter:  ").lower()

    while len(guess) !=1 or not guess.isalpha():
        print("you have entered incorrect input, try again .....")
        guess = input("Please type in your guess letter:  ").lower()
    print(guess)
    print("______________________")

    if guess in correct_letters_keep:
        player_live -= 1
        print(f"You already guessed '{guess}' before! You lose a life. Lives left: {player_live}")
        if player_live == 0:
            print("Game is over.. You LOSE .... HANGMAN !!!!")
            break
        continue  # skip to next round

# check this letter against the word picked in chosen word
    hit =0
    display =""
    for letter in chosen_word:
        if letter == guess:
            print("You have pick a right letter !!!")
            print ("your guess of "+guess +" matches "+letter +" in the word "+chosen_word )
            hit += 1
            display += letter
            correct_letters_keep.append(guess)
            print(f"You hit the correct letter {hit} time(s)")
        elif letter in correct_letters_keep:
            display += letter
        else:
            display += "_"


    if guess != chosen_word:
        player_live -= 1
        print("You have " + str(player_live) + " live(s) left !!!!!!!!")
        print("-------------------------------------------------------------------")
        if player_live == 0:
            print("Game is over..You LOSE .... HANGMAN !!!!")
            game_end = True




    print("These are the blinks filled so far ....")
    print(display)

    if "_" not in display:
        game_end = True
        print("You Win !")
