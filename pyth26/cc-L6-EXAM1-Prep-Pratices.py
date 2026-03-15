"""
Write a math tutor program that randomly generates two numbers (up to three digits) and asks
the user to add them together. If the user adds them correctly, a message prints congratulating
them. If they add the numbers incorrectly, display the correct answer.

"""
import random

def validate(answer):
    while True:
        if answer.isdigit() and 0 < int(answer) < 1998:
            return int(answer)
        print("***Invalid answer or beyond 3 digits ....Please Try Again ......")
        answer = input("Please enter the sum of the two numbers: ")

def generate_problem():
    aa = random.randint(1, 1000)
    bb = random.randint(1, 1000)
    return aa, bb

def ask_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        print("WHAT? I didn't get you. Please enter only 'y' or 'n'.")

def run_problem():
    aa, bb = generate_problem()
    print(f"NUM1 is {aa} and NUM2 is {bb} ... Please add them together")
    print(f"Correct sum of them is : {aa+bb:,}")

    user_input = input("Please enter the sum of the two numbers: ")
    answer = validate(user_input)

    while answer != aa + bb:
        print("Incorrect answer, try again")
        user_input = input("Please enter the sum of the two numbers: ")
        answer = validate(user_input)

    print("Congrats! You got it correct!")

# ---------------- MAIN PROGRAM LOOP ----------------

while True:
    run_problem()
    again = ask_yes_no("Do you want to try another addition problem? (y/n): ")

    if again == "n":
        print("Program ended")
        break