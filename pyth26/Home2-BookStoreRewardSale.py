
# Validate if input 1,2 or 3 for the main menu
def get_validated_option():
    while True:
        print("1. Customer Information")
        print("2. See Today's Sales Total")
        print("3. Quit")
        option = input("Please enter an operation to be performed:   ")
        if option.isdigit() and int(option) > 0 and int(option) < 4:
            return int(option)
        print("***Invalid operation choice.....You must enter option 1, 2 or 3....Please Try Again ......")

# Validate unit book price as a whole number .... not set for two decemal yet
def get_valid_price():
      while True:
        price = input("Please enter a price for the book we are selling:   ")
        if price.isdigit() and int(price) > 0:
            return int(price)
        print("Invalid input, You must enter a valid number for the book price !! Please Try Again ......")

# Validate number of books as a whole number .... reusing the same code as get_valid_price
def get_valid_bookqty():
      while True:
        price = input("Please enter a number of book customer is buying:   ")
        if price.isdigit() and int(price) > 0:
            return int(price)
        print("Invalid input, You must enter a valid number for the book price !! Please Try Again ......")
        

grand_total = 0
op = get_validated_option()
print("The option you picked was: ", op)

while op != 3:
    if op == 1:
        p = get_valid_price()
        q = get_valid_bookqty()
        print(f"Customer wants to buy {q} books each at ${p} ")
        break
    elif op ==2:
        print(f"Grand Total is: ${grand_total}")

print(f"Qutting This Program.....Grand Total is: ${grand_total}")



"""
Pseudo Code

grand_total = 0
loop until user quits

Options:
1. Enter a customer sales info
    a. how many books
    b. set price of the book
    c. calculate sub total and +0.0925 tax
    d. ask member status (member/free/non-member)
        if member   .. total x .9
    final_price = books x qty  x 0.09 (if discount) x 1.0925 (tax) 
    grand_total = grand_total + final_price
    e. calculate points 
        if 1 book = 5 pt for all
        if 2 books = 15 pt for all
        if 3 books = 50 pt (member) or 30 pt (free)
        if 4+ books = 100 pt (member) or 60 pt (free)
    f. print one per row .... # books purchased, subtotal, tax, saved amount (for member only), pts recevied (free/member) and final cost    
2.  print out current amount of grand_total
3.  print grand_total before quitting





"""