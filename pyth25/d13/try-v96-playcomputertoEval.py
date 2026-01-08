"""
Playing computer is an important skill in debugging. You need to be able to go through your code line by line as if you were the computer to help you figure out what is going wrong.

PAUSE 1
Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. Then go ahead and fix the code.

"""
while True: # some validation of invalid input and too crazy of the year entered ....
    try:
        year = int(input("What's your year of birth?  "))
        print(f"You have entered {year} as your year ....")
        if 0 <= year <= 2050:
            break
        else:
            print("Please enter a year you were born between 1960 and 2050 ...")
    except ValueError:
            print("Invalid input, please try again ....")

if year >= 1965 and year <= 1980:
    print("You are a Gen X.")
elif year > 1980 and year <= 1994:   # you must enter a year with in this range and certain numbers are out of this range
    print("You are a millennial.")
elif year > 1994 and year <= 2012:
    print("You are a Gen Z.")
elif year > 2012 and year <= 2024:
    print("you are in Gen Alpha")
elif year > 2024 and year <= 2035:
    print("You are Gen Beta")
elif year > 2035 and year <= 2050:
    print("You are Gen Gimma")
else:
    print("Man, you are OLD !")


