print("Welcome to the rollercoaster !!!")
height = int(input("What is your height in CM?  "))
age = int(input("What is your age?  "))

if height >= 120:
    print("Congrats ! you CAN ride the rollercoaster !!")
    if age < 12:
        print("Your ticket price is $5")
        price = 5

    elif age <= 18:
        print("Your ticket price is $7")
        price =7
    else:
        print("Your ticket price is $12")
        price =12

    photo=input("Do you want to include the exciting photo shot while you were in the rollercoaster? Y/N ")
    if photo == "y":
        print("Your final price is $" +str(price+3))
    else:
        print("Your final price is $" +str(price))


else:
    print("Sorry the policy said you dont have enough height to ride the rollercoaster ..")

