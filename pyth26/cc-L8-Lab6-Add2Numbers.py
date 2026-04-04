import os

def add_pair_number():
    num1 = input("Enter first number to add:  ")
    num2 = input("Enter second number to add: ")
    two_sum = float(num1) + float(num2)
    with open("data\\results.txt", "a") as addfile:
        addfile.write(f"{num1}+{num2}={two_sum}\n")

def print_history():
    print("This is the history of addition operations : ")
    with open("data\\results.txt", "r") as fileb:
        for name in fileb.readlines():
            print(name, end="")
    print()

os.makedirs("data", exist_ok=True)

result = 0
while result != 'q':
    result = input("Press 1 to enter another pair of numbers to add.  Press 2 to view history, q to quit: ")
    if result.isdigit() and int(result) == 1:
        add_pair_number()
    elif result.isdigit() and int(result) == 2:
        print_history()
    else:    
        print("Invalid input ... try again")

