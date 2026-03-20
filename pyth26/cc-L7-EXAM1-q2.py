def get_score():
    while True:

            score = int(input("Enter score for the game: "))
            if score < 0:
                print("Score cannot be negative. Try again.")
            else:
                return score
     
            print("Invalid input. Please enter a valid integer.")

def perform_calculations(scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    return average, highest, lowest

num_games = int(input("How many games did the player play? "))


while num_games <= 0:
    print("Number must be greater than 0")
    num_games = int(input("How many games did the player play? "))

scores = []

# ask for score of each game
for i in range(num_games):
    print("Game", i+1)
    score = get_score()
    scores.append(score)

# calculates average
avg, high, low = perform_calculations(scores)

# display results
print("\nPlayer Statistics")
print("Average Score:", round(avg, 2))
print("Highest Score:", high)
print("Lowest Score:", low)