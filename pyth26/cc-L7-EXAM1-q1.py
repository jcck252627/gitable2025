import random

def flip_coin():
    correct_count = 0
    total_rounds = 8
    history = []

    for i in range(total_rounds):
        while True:
            guess = input("Round " + str(i+1) + " - Enter your guess (head/tail): ").lower()
            if guess == "head" or guess == "tail":
                break
            print("Invalid input, must type 'head' or 'tail', try again...")  # loop back when input is invalid, only head or tail is accepted

        result = random.choice(["head", "tail"])

        if guess == result:  #flag the correct result for later calculation  
            print("Coin toss result: " + result + " ...Correct Guess !\n")
            correct = True
            correct_count += 1
        else:
            print("Coin toss result was " + result + " Wrong Guess !\n")
            correct = False

        history.append([i+1, guess, result, correct])  # store flip coin history into a list
    return history, correct_count, total_rounds

# call function to flip coin 8 times
history, correct_count, total_rounds = flip_coin()

print("")
print("Throw      Correct")
print("------------------")

for record in history:
    throw_text = str(record[0])

    # print aligned columns 
    spaces = " " * (10 - len(throw_text))

    # print Y or N under Correct column
    if record[3] == True:  # extract the result of the each toss from history list , either correct or not
        print(throw_text + spaces + "Y")
    else:
        print(throw_text + spaces + "N")

print (history)
percent = (correct_count / float(total_rounds)) * 100
print("")
print("Final Score: " + str(correct_count) + " correct out of " + str(total_rounds) + " tries")
print("Percentage correct: " + format(percent, ".2f") + "%")
print("")
