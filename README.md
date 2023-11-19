# Python_Intern
In this repository, I have completed the following tasks as part of the codsoft internship for PYTHON PROGRAMMING

1.Simple Calculator (Calculatorcode.py)
   First the two input values and the operation to be performed are obtained from the user.
   Using if else calculate the sum difference product and division of the numbers as per the input given by the user
   Display the result to the user

2.Contact Book (contactbook.py)

1. Contact Class:
   - Defines a Contact class with attributes name, phone_number, email, and address.
   - The __init__ method initializes these attributes when a new Contact object is created.

2. ContactBook Class:
   - Defines a ContactBook class.
   - The __init__ method initializes a list called contacts to store instances of the Contact class.

3. ContactBook Methods:
1. add_contact(self, contact)
     - Appends a given contact to the contacts list.
     - Prints a success message indicating that the contact has been added.

2. view_contacts(self)
     - Displays a list of contacts (names and phone numbers) if there are contacts in the list.
     - Prints a message if no contacts are found.

3. search_contact(self, keyword)
     - Searches for contacts whose names or phone numbers contain the specified keyword.
     - Displays search results, including names and phone numbers.
     - Prints a message if no matching contacts are found.

4. update_contact(self, name, new_phone_number, new_email, new_address)
     - Updates the phone number, email, and address of a contact with the given name.
     - Prints a success message if the contact is found and updated; otherwise, prints a message that the contact is not found.

   - delete_contact(self, name)
     - Deletes a contact with the specified name.
     - Prints a success message if the contact is found and deleted; otherwise, prints a message that the contact is not found.

5. Main Function (`main`):
   - Creates an instance of ContactBook called contact_book.
   - Implements a menu-driven loop where the user can choose various actions related to managing contacts.
   - Choices include adding, viewing, searching, updating, or deleting contacts, as well as exiting the program.

6. Program Execution:
   - Calls the main function if the script is run as the main module (__name__ == "__main__").
  
3.Password Generator: (pwgenerator.py)

1. **Imports:**
   - Imports the `random` module for generating random values.
   - Imports the `string` module, which provides string-related constants.

2. **Password Generation Function (`generate_password`):**
   - Defines a function to generate a random password of a specified length.
   - Uses a combination of ASCII letters, digits, and punctuation for character choices.
   - Utilizes the `random.choice` function to create the password.

3. **Main Function (`main`):**
   - Prompts the user to enter the desired length of the password.
   - Handles potential errors in user input using a `try-except` block.
   - Validates that the entered length is a positive integer.
   - Calls the `generate_password` function and prints the generated password.
   - Displays an error message if the entered value is not a valid integer.

4. **Script Execution Check:**
   - Checks if the script is being run as the main module.
   - If true, calls the `main` function to execute the program.
  
4. Rock Paper Scissors Game: (rps.py)

