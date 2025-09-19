import random
from english_words import get_english_words_set

def get_random_english_word():
    words = get_english_words_set(sources=['web2'], lower=True, alpha=True)
    valid = [w for w in words if len(w) in (3, 4)]
    return random.choice(valid) if valid else None

def get_random_number():
    return random.randint(10, 999)  # Covers 2- and 3-digit numbers

to_continue = True

while to_continue:
    # Generate 3 random words and 3 random numbers
    valid_words = [get_random_english_word() for _ in range(3)]
    valid_numbers = [get_random_number() for _ in range(3)]

    # Display prompt
    print(f'Please input only one of these words: {", ".join(valid_words)}')
    print(f'And input only one of these numbers: {", ".join(map(str, valid_numbers))}')

    # Get user input
    user_word = input("Enter a word: ").strip().lower()
    user_number = input("Enter a number: ").strip()

    # Validate input
    if user_word in valid_words and user_number.isdigit() and int(user_number) in valid_numbers:
        print(f'You have entered the valid input: "{user_word}" and "{user_number}"')
    else:
        print("Invalid input. Please try again.")

    # Ask to continue
    while True:
        continues = input("Do you want to continue running the program? (type in y or n): ").strip().lower()
        if continues == 'y':
            break  # Continue the loop
        elif continues == 'n':
            to_continue = False  # Exit the loop
	    
            break
        else:
            print("Invalid continuation code, please type 'y' or 'n'.")

print("program exited normally per user request ..............")
