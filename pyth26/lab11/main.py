# Import the Contact class from contact.py
from contact import Contact

# Import pickle so we can save data to a file
import pickle


# Load saved contacts from the file
def load_contacts():

   # Try to open the saved file
   try:

      # Open the file in binary read mode
      with open("mydata.dat", 'rb') as file:

         # Load and return the dictionary
         return pickle.load(file)

   # If the file does not exist yet
   except FileNotFoundError:

      # Return an empty dictionary instead
      return {}


# Save contacts into the file
def save_contacts(contacts):

   # Open the file in binary write mode
   with open("mydata.dat", 'wb') as file:

      # Save the dictionary into the file
      pickle.dump(contacts, file)


# Add a new contact
def add(contacts):

   # Ask the user for the contact's name
   name = input("Name: ")

   # Do not allow duplicate names
   if name in contacts:
      print("An entry already exists for that contact!")
      return

   # Ask for the email address
   email = input("Email: ")

   # Create a new Contact object
   entry = Contact(name, email)

   # Keep asking for phone numbers
   while True:

      # Ask for a number
      next_num = input("Enter a phone number (or -1 to stop): ")

      # Stop when the user enters -1
      if next_num == "-1":
         break

      # Add the number to the contact
      entry.add_number(next_num)

   # Add the contact object into the dictionary
   contacts[name] = entry


# Look up a contact by name
def look_up(contacts):

   # Ask the user for a name
   name = input("Enter a name: ")

   # If the contact exists
   if name in contacts:

      # Print the contact information
      print(contacts[name])

   else:
      # Contact was not found
      print("There is no contact with that name")


# Delete a contact
def delete(contacts):

   # Ask which contact to remove
   name = input("Enter a name to remove from your list of contacts: ")

   # Check if the contact exists
   if name in contacts:

      # Show the contact before deleting
      print("Are you sure you want to delete the following contact? ")
      print(contacts[name])

      # Ask for confirmation
      choice = input("'y' or 'n': ")

      # Delete if the user says yes
      if choice == 'y':
         del contacts[name]

      else:
         print("Contact saved in dictionary")

   else:
      print("There is no contact with that name")


# Edit an existing contact
def edit_contact(contacts):

   # Ask for the contact name
   name = input("Enter the name of the contact you want to edit: ")

   # Make sure the contact exists
   if name not in contacts:
      print("There is no contact with that name")
      return

   # Save the contact object into a variable
   entry = contacts[name]

   # Keep editing until the user chooses to stop
   while True:

      # Display current contact information
      print("\nEditing Contact:")
      print(entry)

      # Show menu choices
      print("\n1) Remove a phone number")
      print("2) Add a phone number")
      print("3) Change email address")
      print("4) Change contact name")
      print("5) Stop editing")

      # Ask the user for a choice
      choice = input("Choose an option: ")

      # Remove a phone number
      if choice == "1":

         number = input("Enter the phone number to remove: ")

         # Remove the number from the contact
         entry.remove_number(number)


      # Add a new phone number
      elif choice == "2":

         number = input("Enter the phone number to add: ")

         # Add the new number
         entry.add_number(number)


      # Change the email address
      elif choice == "3":

         new_email = input("Enter the new email address: ")

         # Update the email
         entry.email = new_email


      # Change the contact's name
      elif choice == "4":

         new_name = input("Enter the new contact name: ")

         # Remove old dictionary entry
         contacts.pop(name)

         # Update the contact object's name
         entry.name = new_name

         # Add the contact back using the new name
         contacts[new_name] = entry

         # Update the local variable too
         name = new_name


      # Stop editing
      elif choice == "5":

         print("Finished editing contact.")

         # Exit the loop
         break


      # Handle invalid menu choices
      else:
         print("Invalid option.")


# Main function
def main():

   # Load contacts from the file
   contacts = load_contacts()

   # Main program loop
   while True:

      # Display menu options
      choice = int(input(
         "\nEnter 1) to add a contact, "
         "2) to lookup a contact, "
         "3) to delete a contact, "
         "4) to edit a contact, "
         "5) to quit: "
      ))

      # Add contact
      if choice == 1:
         add(contacts)

      # Look up contact
      elif choice == 2:
         look_up(contacts)

      # Delete contact
      elif choice == 3:
         delete(contacts)

      # Edit contact
      elif choice == 4:
         edit_contact(contacts)

      # Quit the program
      elif choice == 5:
         break

      # Invalid choice
      else:
         print("Invalid option.")

   # Save contacts before closing
   save_contacts(contacts)


# Start the program
main()