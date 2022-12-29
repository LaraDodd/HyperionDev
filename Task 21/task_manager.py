# =====importing libraries===========
from datetime import date

with open("tasks.txt", "r") as f:
    data = f.readlines()

for pos, line in enumerate(data, 1):
    split_data = line.split(", ")
    output = f"------------{pos}------------\n"
    output += f"Username: {split_data[0]}\n"
    output += f"Task title: {split_data[1]}\n"
    output += f"Task description: {split_data[2]}\n"
    output += f"Date assigned: {split_data[3]}\n"
    output += f"Date due: {split_data[4]}\n"
    output += f"Task complete? {split_data[5]}\n"
    output += f"-------------------------\n"
    print(output)

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# read all data in user.txt
with open("user.txt", "r") as f:
    user_data = f.readlines()

# initialise lists to append to
usernames = []
passwords = []

# go through each line in user_data and split the line into a list of username and password, add to respective lists
for line in user_data:
    split_user_data = line.split(", ")
    usernames.append(split_user_data[0])
    passwords.append(split_user_data[1].strip("\n"))

# # put all information into a dictionary
# user_dictionary = {
#     "Usernames": usernames,
#     "Passwords": passwords,
# }
credentials_not_entered = True

#ask user to enter username and password
while credentials_not_entered:
    inputted_username = input("Please enter your username: ")
    inputted_password = input("Please enter your password: ")

    if inputted_password not in passwords and inputted_username not in usernames:
        print("These are both not in our system ")

    for i in range(len(usernames)):

        if inputted_username == usernames[i] and not inputted_password == passwords[i]:
            print("Your password is incorrect try again")

        if inputted_password == passwords[i] and not inputted_username == usernames[i]:
            print("Your username is incorrect try again")

        if inputted_username == usernames[i] and inputted_password == passwords[i]:
            print("please wait while we log you in!!")
            credentials_not_entered = False

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        '''add a new user to the user.txt file'''

        passwords_match = False

        while not passwords_match:
            inputted_new_username = input("Please enter a new username: ")
            inputted_new_password = input("Please enter a new password: ")
            check_password = input("Please confirm your password: ")

            if check_password == inputted_new_password:
                with open("user.txt", "a") as f:
                    f.write(f"\n{inputted_new_username}, {inputted_new_password}")
                passwords_match = True

            else:
                print("Sorry the password you entered does not match the first, please try again")


    elif menu == 'a':
        '''contains code that will allow a user to add a new task to task.txt file'''
        task_to_add = True

        while task_to_add:
            inputted_task_assignee = input("Please enter username of the person whom the task is assigned to: ")
            inputted_task_title = input("Please enter title of the task: ")
            inputted_description = input("Please enter description of the task: ")
            inputted_due_date = input("Please enter due date of task: ")
            today_date = date.today().strftime("%b-%d-%Y")
            task_complete = "No"

            output = f"{inputted_task_assignee}, {inputted_task_title}, {inputted_description}," \
                     f"{inputted_due_date}, {today_date}, {task_complete}"

            with open("tasks.txt", "a") as f:
                f.write(f"\n{output}")

            more_tasks = input("Would you like to add another task? y or n? ")
            if more_tasks == "n":
                task_to_add = False

#
#     elif menu == 'va':
#         pass
#         '''In this block you will put code so that the program will read the task from task.txt file and
#          print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#          You can do it in this way:
#             - Read a line from the file.
#             - Split that line where there is comma and space.
#             - Then print the results in the format shown in the Output 2
#             - It is much easier to read a file using a for loop.'''
#
#     elif menu == 'vm':
#         pass
#         '''In this block you will put code the that will read the task from task.txt file and
#          print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#          You can do it in this way:
#             - Read a line from the file
#             - Split the line where there is comma and space.
#             - Check if the username of the person logged in is the same as the username you have
#             read from the file.
#             - If they are the same print it in the format of Output 2 in the task PDF'''
#
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
