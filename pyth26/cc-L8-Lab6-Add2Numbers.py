import os

# prompt and calculate sum of a pair of numbers then write that into a file called results.txt and append them next time it runs
def add_pair_number():
    num1 = input("Enter first number to add:  ")
    num2 = input("Enter second number to add: ")
    two_sum = float(num1) + float(num2)
    with open("data\\results.txt", "a") as addfile:
        addfile.write(f"{num1}+{num2}={two_sum}\n")

# read the history of the addition operations from a file named result.txt
def print_history():
    print("This is the history of addition operations : ")
    with open("data\\results.txt", "r") as fileb:
        for name in fileb.readlines():
            print(name, end="")
    print()

# ensure data directory/folder exist before writing file
os.makedirs("data", exist_ok=True)

result = ""

# user menu and basic validation
while result != "q":
    result = input("Press 1 to enter another pair of numbers to add.  Press 2 to view history, q to quit: ").strip().lower()
    if result == "1":
        add_pair_number()   # call add_pair_number function
    elif result == "2":
        print_history()    # call print_history function
    elif result == "q":
        print("Good Bye !..")  #kick out of the loop if user chose the quit option
        break
    else:
        print("Invalid input ... try again")  #kick back to the loop if invalid option was entered
