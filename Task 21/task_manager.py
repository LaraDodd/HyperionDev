# =====importing libraries===========
from datetime import date
from tkinter import *
from tkinter import messagebox


# ====Login Section====

def login():
    inputted_username = username.get()
    inputted_password = password.get()

    if inputted_password not in passwords and inputted_username not in usernames:
        messagebox.showinfo("Incorrect Credentials", "These are both not in our system")
        return True

    for i in range(len(usernames)):
        if inputted_username == usernames[i] and not inputted_password == passwords[i]:
            messagebox.showinfo("Incorrect Credentials", "Your password is incorrect try again")
            return True

        if inputted_password == passwords[i] and not inputted_username == usernames[i]:
            messagebox.showinfo("Incorrect Credentials", "Your username is incorrect try again")
            return True

        if inputted_username == usernames[i] and inputted_password == passwords[i]:
            messagebox.showinfo("Login Successful", "Please wait while we log you in!!")
            tkWindow.destroy()
            return False


# read all data in user.txt
with open("user.txt", "r") as f:
    user_data = f.readlines()

# initialise lists to append to and initialise while loop bool
usernames = []
passwords = []

# go through each line in user_data and split the line into a list of username and password, add to respective lists
for line in user_data:
    split_user_data = line.split(", ")
    usernames.append(split_user_data[0])
    passwords.append(split_user_data[1].strip("\n"))

# set up tk window
tkWindow = Tk()
tkWindow.geometry('250x100')
tkWindow.title('Task Manager Login')

# username label and text entry box
Label(tkWindow, text="User Name").grid(row=0, column=500)
username = StringVar()
Entry(tkWindow, textvariable=username).grid(row=0, column=600)

# password label and password entry box
Label(tkWindow, text="Password").grid(row=1, column=500)
password = StringVar()  # holder for string variables
Entry(tkWindow, textvariable=password).grid(row=1, column=600)

# login button
Button(tkWindow, text="Login", command=login).grid(row=4, column=600)

tkWindow.mainloop()
inputted_username = username.get()
inputted_password = password.get()
print(inputted_password)

# ========choose option section ==========

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if inputted_username == "admin":
        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.

        # set up tk window
        tkWindow = Tk()
        tkWindow.geometry('250x250')
        tkWindow.title('Admin Options')

        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my tasks
        s - Display statistics
        e - Exit
        : ''').lower()

    else:
        menu = input('''Select one of the following Options below:
                a - Adding a task
                va - View all tasks
                vm - View my tasks
                e - Exit
                : ''').lower()

    # add a new user to the user.txt file
    if menu == 'r':

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

    # contains code that will allow a user to add a new task to task.txt file
    elif menu == 'a':
        task_to_add = True

        while task_to_add:
            inputted_task_assignee = input("Please enter username of the person whom the task is assigned to: ")
            inputted_task_title = input("Please enter title of the task: ")
            inputted_description = input("Please enter description of the task: ")
            inputted_due_date = input("Please enter due date of task: ")
            today_date = date.today().strftime("%b-%d-%Y")
            task_complete = "No"

            output = f"{inputted_task_assignee}, {inputted_task_title}, {inputted_description}, " \
                     f"{inputted_due_date}, {today_date}, {task_complete}"

            with open("tasks.txt", "a") as f:
                f.write(f"\n{output}")

            more_tasks = input("Would you like to add another task? y or n? ")
            if more_tasks == "n":
                task_to_add = False

    # this will read the task from task.txt file and print all tasks to the console in the format of Output 2
    # in the task PDF(i.e. include spacing and labelling)
    elif menu == 'va':
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

    # this will read the task from task.txt file and print just the tasks of the current user to the console
    # in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
    elif menu == 'vm':

        with open("tasks.txt", "r") as f:
            data = f.readlines()

        for pos, line in enumerate(data, 1):
            split_data = line.split(", ")

            if split_data[0] == inputted_username:
                output = f"------------{pos}------------\n"
                output += f"Username: {split_data[0]}\n"
                output += f"Task title: {split_data[1]}\n"
                output += f"Task description: {split_data[2]}\n"
                output += f"Date assigned: {split_data[3]}\n"
                output += f"Date due: {split_data[4]}\n"
                output += f"Task complete? {split_data[5]}\n"
                output += f"-------------------------\n"
                print(output)

    # display total number of tasks and total number of users
    elif menu == "s":
        with open("tasks.txt", "r") as tasks:
            num_tasks = 0
            for line in tasks:
                num_tasks += 1

        with open("user.txt", "r") as users:
            num_users = 0
            for line in users:
                num_users += 1

        print(f"Number of users: {num_users}")
        print(f"Number of tasks: {num_tasks}")

    # exit the code
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
