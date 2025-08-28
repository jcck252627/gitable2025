import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

combined_pool =[letters, numbers,symbols]
print(combined_pool)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?  \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Flatten the list for random selections
flat_list = [item for sublist in combined_pool for item in sublist]
print(flat_list)

#easier version where the password generated according to the order of user input
print("____________________________")
print("This is the easier versin of the password requested where we have letters, followed by symbols then numbers ......")
easy_password =""
for letter_r in range (1, nr_letters+1):
    ran_letter= random.choice(letters)
    easy_password = easy_password +ran_letter

for symbols_r in range (1, nr_symbols+1):
    ran_symbols = random.choice(symbols)
    easy_password = easy_password +ran_symbols

for numbers_r in range (1, nr_numbers+1):
    ran_numbers = random.choice(numbers)
    easy_password = easy_password +ran_numbers

print("The easy version of the password generated this time is:  "+easy_password)


#Harder version where the password generated independent to the order of user input


# Pick a random element
# random_element = random.choice(flat_list)
# print("Random element:", random_element)
