# This class stores information about one contact.
# Each contact has:
# - a name
# - an email
# - a list of phone numbers

class Contact:

   # Constructor method
   # Runs automatically when a new Contact object is created
   def __init__(self, name, email):

      # Save the contact's name
      self._name = name

      # Save the contact's email
      self._email = email

      # Create an empty list for phone numbers
      self._phone_numbers = []


   # Add a phone number to the list
   def add_number(self, phone_number):

      # Check if the number already exists
      if phone_number in self._phone_numbers:
         print("That number is already in the list!")

      else:
         # Add the number to the list
         self._phone_numbers.append(phone_number)


   # Remove a phone number from the list
   def remove_number(self, phone_number):

      # Only remove it if it exists
      if phone_number in self._phone_numbers:
         self._phone_numbers.remove(phone_number)


   # Getter method for phone numbers
   @property
   def phone_numbers(self):
      return self._phone_numbers


   # Getter method for name
   @property
   def name(self):
      return self._name


   # Getter method for email
   @property
   def email(self):
      return self._email


   # Setter method for email
   # Allows us to change the email later
   @email.setter
   def email(self, email):
      self._email = email


   # Setter method for name
   # Allows us to change the contact name later
   @name.setter
   def name(self, name):
      self._name = name


   # Special method that controls how the object prints
   def __str__(self):

      # Start building the string
      return_string = "Name: " + self._name + "\n"

      # Add heading for phone numbers
      return_string += "Numbers:\n"

      # Loop through every phone number in the list
      for num in self._phone_numbers:

         # Add each number to the string
         return_string += "\t" + num + "\n"

      # Add the email to the string
      return_string += "Email: " + self._email

      # Return the finished string
      return return_string