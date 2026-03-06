
import random

# get name from user
def get_name ():
    name = input("Enter Your Name:  ")
    return name

# get email from user
def get_email ():
    email = input("Enter Your Email Address: ")
    return email

# generate a random 4-digit number as the company ID
def calculate_id ():
    id = random.randint(1000, 9999)
    return id

# call the above functions and return 3 values
def get_account ():
    x   =   get_name()
    y   =   get_email()
    z=    calculate_id()
    return x,y,z

# capture the account info as a list
account = get_account()
print("\n")

# save each value from the list .... as 3 indivual variables and output 
name = account[0]
email   = account[1]
id = account[2]
print ("Name: ", name)
print ("Email: ", email)
print ("Company ID: ", id)

