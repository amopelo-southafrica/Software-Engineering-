"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Initialise the instance variables for each email.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Create the 'mark_as_read()' method to change the 'has_been_read'
    # instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

inbox = []

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email_1 = Email("amopelo@gmail.com", "New phone", "Hi your phone is here")
    email_2 = Email("adamjoko@gmail.com", "New phone", "Yo, wassup")
    email_3 = Email("jamesmiller@gmail.com", "New phone", "are you here?")
    inbox.extend([email_1, email_2, email_3])
    
def list_emails():
    for index, email in enumerate(inbox,start=0):
        print(f"{index}: {email.subject_line}")

def read_email(index):
    try:
        email = inbox[index]
        print("\n----- EMAIL OPENED -----")
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Message:\n{email.email_content}")
        print("------------------------")

        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")

    except IndexError:
        print("\nNo email exists at that index.\n")
while True:
    print("\nWhat would you like to do?")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit")

    user_choice = input("\nEnter selection: ")

    if user_choice == "1":
        try:
            index = int(input("\nEnter email index to read: "))
            read_email(index)
        except ValueError:
            print("\nPlease enter a valid number.\n")

    elif user_choice == "2":
        view_unread_emails()

    elif user_choice == "3":
        print("\nExiting application. Goodbye!\n")
        break

    else:
        print("\nInvalid option. Try again.\n")
        
