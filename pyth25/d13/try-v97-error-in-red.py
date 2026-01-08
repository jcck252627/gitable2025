
age = -100
try:
    while age <= 0:
        age = int(input("How old are you?   "))
        if age <= 0:
            print("Try again, ago cannot be less than 1")
except ValueError:
    print("You have typed in a invalid input, please try to type in an integer ")
    age = int(input("How old are you?   "))

if age >= 18:
    print(f"You can drive at age {age}.")
