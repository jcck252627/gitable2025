import os

def add_employee():
    name = input("Enter the employee's name: ")
    with open("data\\employees.txt", "a") as fileb:
        fileb.write(name+"\n")

def print_employee():
    print("This is a list of employees: ")
    with open("data\\employees.txt", "r") as fileb:
        for name in fileb.readlines():
            print(name, end="")
    print()


os.makedirs("data", exist_ok=True)

result = 0
while result != 'q':
    result = input("Press 1 to enter another employee, q to quit: ")
    if result.isdigit() and int(result) == 1:
        add_employee()
    elif result.isdigit() and int(result) == 2:
        print_employee()
    else:    
        print("nothing being input ... try again")

with open("data\\sample.txt", "w") as file:
    file.write("Hello World\n")
    file.write("How are you?\n")
    file.write("Good bye !\n")
    file.write("...Hey? still there ?")

with open("data\\sample.txt", "r") as file:
    filetxt=file.read()
    print(filetxt)

print("==========================================")
with open("data\\sample.txt", "r") as file:
    for line in file.readlines():
        print(line, end="")
