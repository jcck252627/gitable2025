
import os

os.makedirs("data", exist_ok=True)  # folder create/existing
FILENAME = r"..\data\library.txt"   # file named library.txt

# Load data from file library.txt
def load_inventory():
    inventory = {}  # initialize dictionary data structure
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:  # read and looping the data file and loading them into the dictorionary
            for line in file:
                title, count = line.strip().split(",")  # extract title and count values separate by commas
                inventory[title] = int(count)
    return inventory


# Save data to file and looping through the file
def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        for title, count in inventory.items():
            file.write(f"{title},{count}\n")


# Add book function with some basic validation
def add_book(inventory):
    title = input("Enter book title: ").strip()
    
    try:
        copies = int(input("Enter number of copies to add: "))
    except ValueError:
        print("Invalid number.")
        return

    if title in inventory:
        inventory[title] += copies
    else:
        inventory[title] = copies

    print(f"Updated '{title}' to {inventory[title]} copies.")



# Find book from user input title
def find_book(inventory):
    title = input("Enter book title to find: ").strip()

    if title in inventory:
        print(f"'{title}' has {inventory[title]} copies in stock.")
    else:
        print("No copies in stock.")


# Remove book from user input title
def remove_book(inventory):
    title = input("Enter book title to remove: ").strip()

    if title not in inventory:
        print("Book not found.")
        return

    if inventory[title] == 0:
        print("Cannot remove. No copies left.")
        return

    # deduct only one copy from inventory of an existing book 
    inventory[title] -= 1
    print(f"Removed one copy of '{title}'. Remaining: {inventory[title]}")

    # If now copies reaches zero, prompt next action
    if inventory[title] == 0:
        choice = input("No copies left. Keep in system? (yes/no): ").lower()

        if choice == "no":
            del inventory[title]
            print(f"'{title}' now removed from inventory.")




inventory = load_inventory()

while True:
        print("\nWelcome to the Library Inventory System")
        print("1. Add Book")
        print("2. Find Book")
        print("3. Remove Book")
        
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(inventory)
        elif choice == "2":
            find_book(inventory)
        elif choice == "3":
            remove_book(inventory)
        elif choice == "4":
            save_inventory(inventory)
            print("Inventory saved. Goodbye!")
            break
        elif choice == "00":  # debug mode
            print("hidden mode to display database file:\n")

            with open(FILENAME, "r") as fileb:
                for line in fileb:
                    print(line, end="")
  
        else:
            print("Invalid option. Try again.")


