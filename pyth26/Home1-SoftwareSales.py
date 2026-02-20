# home work #1 ... Software Sales 

total_price = 0
unit_price = 99

print("\n")
print ("*************Welcome to the SoftwareBox SuperStore ***************")

while True:
    quantity = input("Please enter a quantity (whole number only) of software package(s) to order: ")

    # Validate input
    if quantity.isdigit():
        quantity = int(quantity)  
        break
    else:
        print("Invalid input. Please enter a whole number for quantity only.")

print(f"**You are ordering quantity:  {quantity}")
print(f'**The retail price for the software package is:   {unit_price}')

if  quantity <= 9:
        print("**You are ordering of quantity less than 10, Sorry.. there is no discount applied")
        total_price = unit_price * quantity 
        print(f'Your total price is:    ${total_price:,.2f}')
    
elif  10 <= quantity <= 19:
        print("**You are ordering a quantity between 10-19 ... Congratulations, you have scored a 10% discount !")
        total_price = (unit_price * quantity)*0.9 
        print(f'Your total price is:    ${total_price:,.2f}')

elif  20 <= quantity <= 49:
        print("**You are ordering a quantity between 20-49 ... Congratulations, you have scored a 20% discount !")
        total_price = (unit_price * quantity)*0.8
        print(f'Your total price is:    ${total_price:,.2f}')

elif  50 <= quantity <= 99:
        print("**You are ordering a quantity between 50-99 ... Congratulations, you have scored a 30% discount !")
        total_price = (unit_price * quantity)*0.7 
        print(f'Your total price is:    ${total_price:,.2f}')

else:
        print("**You are ordering a quantity of 100 or more ... Congratulations, you have scored a MAX 40% discount !")
        total_price = (unit_price * quantity)*0.6 
        print(f'Your total price is:    ${total_price:,.2f}')