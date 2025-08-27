print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L .. if Y will add $2 for small and $3 for medium and large pizza  ")
add_pepperoni = input("Do you want pepperoni? Y or N ..if Y will add $2 for small and $3 for medium and large pizza   ")
extra_cheese = input("Do you want extra cheese? Y or N ...if Y will add $1  ")
# Don't change the code above 

#Write your code below this line 
price = 0

if size == "S" or size=="s":
    price += 15
    print(f"your pizza cost is: ${price}")
    if add_pepperoni == "Y" or add_pepperoni=="y":
        price += 2
        print("You have selected to add pepperoni on your small pizza")

elif size == "M" or size=="m":
    price += 20
    print(f"your pizza cost is: ${price}")
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3
        print("You have selected to add pepperoni on your large or medium pizza")

elif size == "L" or size=="l":
    price += 25
    print(f"your pizza cost is: ${price}")
    if add_pepperoni == "Y" or add_pepperoni == "y":
        price += 3
        print("You have selected to add pepperoni on your large or medium pizza")

if extra_cheese == "Y" or extra_cheese == "y":
    price += 1

print(f"Your final bill is: ${price}.")
