
import os

def lookup_employee():
    id_search = input("Please enter a positive integer of an employee ID to look up: ")

    if not id_search.isdigit():
        print("Invalid ID. Please enter a numeric value.")
        return

    found = False

    with open("data\\employees.txt", "r") as fileb:
        for line in fileb:
            parts = line.strip().split()
            emp_id = parts[0]
            name = " ".join(parts[1:])

            if emp_id == id_search:
                print(f"Found: {emp_id} {name} \n")
                found = True
                break

    if not found:
        print("Employee ID not found")


def lookup_id():
    firstname = input("Please enter the first name of an employee to look up: ")
    lastname = input("Please enter the last name of an employee to look up: ")

    print(f"You have entered to search for {firstname} {lastname}")

    found = False

    with open("data\\employees.txt", "r") as fileb:
        for line in fileb:
            parts = line.strip().split()
            emp_id = parts[0]
            name = " ".join(parts[1:])

            # match first/last name
            if len(parts) >= 3:
                first = parts[1]
                last = parts[-1]

                if (first.lower() == firstname.lower() and 
                    last.lower() == lastname.lower()):
                    print(f"Found: {emp_id} {name}\n")
                    found = True
                    break
    if not found:
        print("Employee name not found ... \n")



result = 0
while result != 'q':
    print("Enter 1 to lookup an employee NAME based on ID")
    print("Enter 2 to lookup an employee ID based on Name")
    print("Enter q to quit\n")

    result = input("Your choice: ")

    if result == '1':
        lookup_employee()
    elif result == '2':
        lookup_id()
    elif result == 'q':
        break
    else:    
        print("Invalid input ... try again")
