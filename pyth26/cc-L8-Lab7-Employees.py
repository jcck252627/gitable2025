
import os
# PS ::: this program only read into file  data\\employee.txt, this file must first exist with pre filled data before running this program

# this function read the file and search for specific ID
def lookup_employee():
    id_search = input("Please enter a positive integer of an employee ID to look up: ")
# validate if a valid ID has been entered
    if not id_search.isdigit():
        print("Invalid ID. Please enter a numeric value.")
        return

    found = False

    with open("data\\employees.txt", "r") as fileb:
        for line in fileb:
            parts = line.strip().split()
            emp_id = parts[0]   #extract the first item of a line as the employee ID and save as emp id variable
            name = " ".join(parts[1:])  #extract the rest part of a line as the employee Name and save as name variable
# find match by ID then prints the associated first and last name
            if emp_id == id_search:
                print(f"Found: {emp_id} {name} \n")
                found = True
                break
    if not found:
        print("Employee ID not found")

# this function searches the file and finds employee by exact FIRST and LAST name only
def lookup_id():
    # get user input and split into words
    firstname_input = input("Please enter the first name of an employee to look up: ").strip().split()
    lastname_input = input("Please enter the last name of an employee to look up: ").strip().split()

    # only use first word of first name and last word of last name
    firstname = firstname_input[0].lower()  #extract the first item of what user entered as the employee first name and nothing else
    lastname = lastname_input[-1].lower()  #extract the last item of what user entered as the employee last name and nothing else 
# output what was being searched 
    print(f"You have entered to search for {firstname.capitalize()} {lastname.capitalize()}")

    found = False

    with open("data\\employees.txt", "r") as fileb:
        for line in fileb:
            parts = line.strip().split()

            # must contain at least: ID + first + last
            if len(parts) < 3:
                continue

            emp_id = parts[0]
            first = parts[1].lower()
            last = parts[-1].lower()
            full_name = " ".join(parts[1:])

            # match ONLY first and last name
            if first == firstname and last == lastname:
                print(f"Found: {emp_id} {full_name}\n")
                found = True
                break

    if not found:
        print("Employee name not found ...\n")

# main function to print menu and basic option input validation ...and then call a function per option
result = 0
while result != 'q':
    print("Enter 1 to lookup an employee based on ID")
    print("Enter 2 to lookup an employee based on First and Last Name")
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
