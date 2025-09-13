#excerise.py

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

while True:
    try:
        num = int(input("Put in a number: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("You have typed an invalid input. Please try again with an integer.")

print(odd_or_even(num))
