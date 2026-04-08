import os

os.makedirs("data", exist_ok=True)  # Making sure a "data" diretory is there... for read and write to the scores.txt file

# Global constant defined 3-letter month formats for each month and number of days in a directionary struction for later verfication
MONTHS = {
    "jan": 31, "feb": 29, "mar": 31, "apr": 30,
    "may": 31, "jun": 30, "jul": 31, "aug": 31,
    "sep": 30, "oct": 31, "nov": 30, "dec": 31
}

# This function validates if the exact mon/day user entered was already on file, return boolean result
def score_exist_that_date(month, day):
# define path to the data/scores.txt file
    filepath = "data/scores.txt"
# kick out of this function if the file is not even there 
    if not os.path.isfile(filepath):
        return False   
#open and reading the scores.txt file
    with open(filepath, "r") as file:
# loop that going through each line of the file and looking for matching month and day of the month
        for line in file:
            parts = line.split()
            if len(parts) >= 2:
                file_month = parts[0].lower()
                file_day = parts[1].replace(":", "")
                if file_month.startswith(month) and file_day == str(day):
                    return True
    return False
# This function is called to add score entry or entries in the scores.txt file
def add_score():
    os.makedirs("data", exist_ok=True)
    filepath = "data/scores.txt"
# prompt user for a 3 letter month input with basic validation
    while True: 
        month = input("Enter 3-letter month abbreviation (Jan, Feb, Mar...): ").strip().lower()
        if month in MONTHS: 
            break
        print("Invalid month... try again")

# prompt user for a 3 letter month input with basic validation
    end_day = MONTHS[month]

    while True:
        day = input(f"Enter a date between 1 and {end_day}: ").strip()
        if day.isdigit() and 1 <= int(day) <= end_day:
            day = int(day)
            break
        print("Invalid date... try again")

# calling the score_exist_that_date function to check existing score on that date ... reprompt if yes
    if score_exist_that_date(month, day): 
        print("Scores already existed that day, no new scores have been entered.")
        return
# save scores entered for this run of the function to a list
    scores = []
# enter score between 0 and 300 with validations
    while True:
        s = input("Enter a score between 0 and 300 (or 'done' to finish): ").strip().lower()
        if s == "done":
            break
        if s.isdigit() and 0 <= int(s) <= 300:
            scores.append(int(s))
        else:
            print("Invalid score... try again")
    if not scores:
        print("No scores entered.")
        return
# open file score.txt and append scores entered per that date, scores separated by comma
    with open(filepath, "a") as file:
        month_cap = month.capitalize()
        score_str = ",".join(str(x) for x in scores)
        file.write(f"{month_cap} {day} : {score_str}\n")

    print("Scores saved successfully!")

# this function open and print existing score entries from file scores.txt
def view_score():
    filepath = "data/scores.txt"
    # Check if file exists first and direct user to ADD score option first
    if not os.path.isfile(filepath):
        print("Scores file not found... Please select option 2 to ADD score first.")
        return   # kick back to main program after reading the data file
    print("This is what the scores file looks like.............\n")
    with open(filepath, "r") as fileb:
        for line in fileb:
            print(line, end="")
    print()

# this function read all scores and calculate grand average out all scores
def average_scores():
    filepath = "data/scores.txt"
    # Check scores.txt file even exists
    if not os.path.isfile(filepath):
        print("Scores file not found... Please select option 2 to ADD score first.")
        return

    total_scores = 0
    total_count = 0

    with open(filepath, "r") as file:
        for line in file:
            
            if ":" not in line:
                continue
            parts = line.split(":")
            score_part = parts[1].strip() # starting extracting 2nd item of the line to be scores, separated by colon
            scores = score_part.split(",") # extract each score separated by commas
            for s in scores:  # sum up the scores and increase the counter for each score added
                s = s.strip()
                if s.isdigit():
                    total_scores += int(s)
                    total_count += 1
# calculate average once out of the loop
    average = total_scores / total_count
    print(f"Average score across all dates: {average:.2f}")

# This function will pick out specifically score 300 and increase the counter of number of times it appears
def num_300():
    filepath = "data/scores.txt"

    # Check if scores.txt file even exists
    if not os.path.isfile(filepath):
        print("Scores file not found... Please select option 2 to ADD score first.")
        return
# start the counter of the 300-score with zero
    count_300 = 0
    with open(filepath, "r") as file:
        for line in file:
            if ":" not in line:
                continue
            parts = line.split(":")
            score_part = parts[1].strip()
            scores = score_part.split(",")
            for s in scores:
                if s.strip() == "300":
                    count_300 += 1
    print(f"Number of times score 300 was entered: {count_300}")

# main function , prints menu system and basic validations
result = ""
while result != "5":
    print("***Options avaiable***")
    print("1. View Score")
    print("2. Add Score")
    print("3. Average Score")
    print("4. Score 300 History")
    print("5. Quit")
    result = input("***Enter the option you wish: ").strip().lower()
    if result == "1":               # view_score function is called
        view_score()
    elif result == "2":             # add_score function is called
        add_score()
    elif result == "3":            # average_score function is called
        average_scores()
    elif result == "4":            # num_300 function is called
        num_300 ()
    elif result == "5":             # Quit
        print("\nGood Bye !..")
        break
    else:
        print("Invalid input ... try again")
