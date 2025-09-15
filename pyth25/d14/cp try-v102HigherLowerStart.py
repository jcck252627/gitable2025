import random
import art
import game_data

# pick two random dictionary entries as an inital comparison mark them as "entry xxx position A" and "entry yyy position B"

# have user input A or B to select which one guessing to have more followers, start with score zero

# compare the two dictionary entry in its "followers" field and determine which one is greater

# switch the position B to A if the dictionary entry B wins and replace the entry in B with another random entry

# if user guessed it right ...increment the score  ... if not display the current score and end the game

# run compare again and run switch again


# pick and display two random dictionary entries

print(art.logo+"\n")
picks = random.sample(game_data.data, 2)

formatted = []
for entry in picks:
    formatted.append(", ".join(f"{k}: {v}" for k, v in entry.items() if k != "follower_count"))

# Join with VS
print(art.vs.join(formatted))

print("\n")
print(formatted[0])
print(formatted[1])

