import os

os.makedirs("data", exist_ok=True)  # MAKE SURE DATA DIRECTORY IS THERE

MONTHS = {
    "jan": 31, "feb": 29, "mar": 31, "apr": 30,
    "may": 31, "jun": 30, "jul": 31, "aug": 31,
    "sep": 30, "oct": 31, "nov": 30, "dec": 31
}

def score_exist_that_date(month, day):
    """Return True if the same month/day already exists in scores.txt"""
    filepath = "data/scores.txt"

    if not os.path.isfile(filepath):
        return False   # file not created yet → no duplicates

    with open(filepath, "r") as file:
        for line in file:
            # Example line: "Feb 15 : 200,199,145"
            parts = line.split()
            if len(parts) >= 2:
                file_month = parts[0].lower()
                file_day = parts[1].replace(":", "")
                if file_month.startswith(month) and file_day == str(day):
                    return True

    return False

def add_score():
    os.makedirs("data", exist_ok=True)
    filepath = "data/scores.txt"

    # -------------------------
    # 1. Ask for month
    # -------------------------
    while True:
        month = input("Enter 3-letter month abbreviation (Jan, Feb, Mar...): ").strip().lower()
        if month in MONTHS:
            break
        print("Invalid month... try again")

    # -------------------------
    # 2. Ask for date
    # -------------------------
    max_day = MONTHS[month]

    while True:
        day = input(f"Enter a date between 1 and {max_day}: ").strip()
        if day.isdigit() and 1 <= int(day) <= max_day:
            day = int(day)
            break
        print("Invalid date... try again")

    # -------------------------
    # 3. Check if scores already exist for that date
    # -------------------------
    if score_exist_that_date(month, day):
        print("Scores already existed that day, no new scores have been entered.")
        return

    # -------------------------
    # 4. Enter scores
    # -------------------------
    scores = []

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

    # -------------------------
    # 5. Append to file
    # -------------------------
    with open(filepath, "a") as file:
        month_cap = month.capitalize()
        score_str = ",".join(str(x) for x in scores)
        file.write(f"{month_cap} {day} : {score_str}\n")

    print("Scores saved successfully!")



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

def average_scores():
    filepath = "data/scores.txt"

    # Check file exists
    if not os.path.isfile(filepath):
        print("Scores file not found... Please select option 2 to ADD score first.")
        return

    total_scores = 0
    total_count = 0

    with open(filepath, "r") as file:
        for line in file:
            # Example line: "Feb 15 : 145,123,222,45"
            if ":" not in line:
                continue

            parts = line.split(":")
            score_part = parts[1].strip()

            # Split into individual scores
            scores = score_part.split(",")

            for s in scores:
                s = s.strip()
                if s.isdigit():
                    total_scores += int(s)
                    total_count += 1

    if total_count == 0:
        print("No scores found in file.")
        return

    average = total_scores / total_count
    print(f"Average score across all dates: {average:.2f}")


def num_300():
    filepath = "data/scores.txt"

    # Check file exists
    if not os.path.isfile(filepath):
        print("Scores file not found... Please select option 2 to ADD score first.")
        return

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
       
    



result = ""

while result != "5":
    print("***Options avaiable***")
    print("1. View Score")
    print("2. Add Score")
    print("3. Average Score")
    print("4. Score 300 History")
    print("5. Quit")
    result = input("***Enter option you wish: ").strip().lower()
    if result == "1":               # view score function is called
        view_score()
    elif result == "2":             # add score function is called
        add_score()
    elif result == "3":            # average score function is called
        average_scores()
    elif result == "4":            # num 300 function is called
        num_300 ()
    elif result == "5":             # Quit
        print("\nGood Bye !..")
        break
    else:
        print("Invalid input ... try again")
