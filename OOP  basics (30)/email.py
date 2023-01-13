class Email:
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self) -> None:
        """This function changes has_been_read to True"""
        self.has_been_read = True

    def mark_as_spam(self) -> None:
        """This function changes is_spam to True"""
        self.is_spam = True


class Inbox:
    def __init__(self):
        self.inbox_list = []

    def add_email(self, from_address: str, subject_line: str, email_contents: str) -> None:
        """takes in the email contents, subject line and email address, makes a new email object and stores in
        inbox list

        Args: from_address: string input by user, denoting the email address of the sender
              subject_line: string input by user, denoting the email subject
              email_contents: string input by user, denoting the email contents"""
        email_object = Email(from_address, subject_line, email_contents)
        self.inbox_list.append(email_object)

    def list_messages_from_sender(self, sender_address: str) -> str:
        """returns string showing all subject lines in emails from a specific sender, and a corresponding index no.

        Args: sender_address: string input by user, indicating the email address of the sender"""
        sender_subject_email_list = [email.subject_line for email in self.inbox_list if
                                     email.from_address == sender_address]

        output = ""
        for pos, subject in enumerate(sender_subject_email_list):
            output += f"{pos}\t{subject}\n"
        return output

    def get_email(self, sender_address: str, index: int) -> str:
        """returns the email subject at a specific index from a specific user

        Args: sender_address: string input by user, indicating the email address of the sender
              index: int denoting the index number of specified email"""
        sender_subject_email_list = [email.subject_line for email in self.inbox_list if
                                     email.from_address == sender_address]
        return sender_subject_email_list[index]

    def mark_as_spam(self, sender_address: str, index: int) -> None:
        """marks an email from specific sender at specific index as spam

        Args: sender_address: string input by user, indicating the email address of the sender
              index: int denoting the index number of specified email"""
        sender_email_list = [email for email in self.inbox_list if email.from_address == sender_address]
        sender_email_list[index].mark_as_spam()

    def get_unread_emails(self) -> str:
        """returns a string containing a list of all unread emails, only subject is shown"""
        list_of_unread_emails = [email.subject_line for email in self.inbox_list if email.has_been_read is False]
        output = ""
        for subject in list_of_unread_emails:
            output += f"{subject}\n"
        return output

    def get_spam_emails(self) -> str:
        """returns a string containing a list of all spam emails, only subject is shown"""
        list_of_spam_emails = [email.subject_line for email in self.inbox_list if email.is_spam is True]
        output = ""
        for subject in list_of_spam_emails:
            output += f"{subject}\n"
        return output

    def delete(self, sender_address: str, index: int) -> None:
        """deletes an email from the self.inbox_list for specific sender at specific index

        Args: sender_address: string input by user, indicating the email address of the sender
              index: int denoting the index number of specified email"""
        sender_email_list = [email for email in self.inbox_list if email.from_address == sender_address]
        selected_email_object = sender_email_list[index]
        for email in self.inbox_list:
            if email == selected_email_object:
                self.inbox_list.remove(selected_email_object)


# ================= MAIN CODE ==================
usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

# An Email Simulation
# create inbox class
inbox = Inbox()

user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # create a new Email object within the Inbox class and add to the inbox email list by calling the add_email
        # method within inbox
        inbox.add_email(subject_line=subject_line, from_address=sender_address, email_contents=contents)

        # Print a success message
        print("Email has been added to inbox.")

    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        # call the list_messages_from_sender method from the Inbox class
        sender_emails = inbox.list_messages_from_sender(sender_address=sender_address)

        # Now list all emails from this sender
        print(sender_emails)

    elif user_choice == "r":
        # Read an email
        # Step 1: ask user input
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        sender_emails = inbox.list_messages_from_sender(sender_address=sender_address)
        print(sender_emails)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))

        # Step 4: display the email
        email = inbox.inbox_list[email_index]
        email.mark_as_read()
        print(email.email_contents)
        print("This email is now marked as read")

    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: ask user to input sender address
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        sender_emails = inbox.list_messages_from_sender(sender_address=sender_address)
        print(sender_emails)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))

        # Step 4: mark the email as spam
        inbox.mark_as_spam(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been marked as spam")

    elif user_choice == "gu":
        # List all unread emails
        unread_emails = inbox.get_unread_emails()
        print(unread_emails)

    elif user_choice == "gs":
        # List all spam emails
        spam_emails = inbox.get_spam_emails()
        print(spam_emails)

    elif user_choice == "e":
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email
        # Step 1: ask user to input sender address
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        sender_emails = inbox.list_messages_from_sender(sender_address=sender_address)
        print(sender_emails)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        inbox.delete(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been deleted")

    else:
        print("Oops - incorrect input")
