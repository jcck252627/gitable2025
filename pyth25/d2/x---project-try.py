
print("Welcome to the TIP CALCULATOR !!!")

# Convert input strings to appropriate numeric types
bill = float(input("What was the total bill? $"))
percent = float(input("How much tip would you like to give? (in percentage): "))
people = int(input("How many people are splitting the bill? "))

# Calculate tip and total per person
percent_number = percent / 100
finalperc = 1 + percent_number
finalbill = (bill * finalperc) / people

# Format the result to 2 decimal places
print(f"I have calculated, each of you should pay: ${finalbill:.2f}")


