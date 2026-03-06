
import random
import re

def get_name ():
    while True:
        name = input("Enter Your Name: ").strip()
        
        # check that name only contains letters and spaces
        if name.replace(" ", "").isalpha():
            return name
        
        print("Invalid name. Only letters and spaces are allowed.")
    return name

def get_email ():
    while True:
        email = input("Enter Your Email Address: ").strip()

        # simple email validation pattern
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if re.match(pattern, email):
            return email
        
        print("Invalid email format. Example: user@domain.com")
    return email

def calculate_id ():
    id = random.randint(1000, 9999)
    return id

def get_account ():
    x   =   get_name()
    y   =   get_email()
    z=    calculate_id()
    print("\nAccount Created")
    print("Name:", x)
    print("Email:", y)
    print("ID:", z)
    return x,y,z
    
account = get_account()
print("\n")

name = account[0]
email   = account[1]
id = account[2]
print ("Name: ", name)
print ("Email: ", email)
print ("Company ID: ", id)



