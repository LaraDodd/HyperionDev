# =====importing libraries===========
from datetime import date
from tkinter import *
from tkinter import messagebox


# functions
def admin_menu():
    """this function returns a string menu for the admin"""
    return '''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - View my tasks
            gr - Generate reports - generates user overview and task overview.
            s - Display statistics - adds total no. users and total no. tasks stats to the reports
            e - Exit
            : '''


def user_menu():
    """this function returns a string menu for the non-admin users"""
    return '''Select one of the following Options below:
                a - Adding a task
                va - View all tasks
                vm - View my tasks
                e - Exit
                : '''


def user_already_in_db(user):
    """takes in user argument and returns a boolean value indicated whether user already in databse"""
    with open("user.txt", "r") as users:
        user_data = users.read()
        if f"{user}," in user_data:
            return True
        else:
            return False


def reg_user():
    """asks for new user, adds a new user to the user.txt file if user not already in database
    checks if passwords match, if they don't, asks user to try again"""
    passwords_match = False

    while not passwords_match:

        inputted_new_username = input("Please enter a new username: ")

        # check if entered username already in users.txt, if it is, ask user to enter different username
        if user_already_in_db(inputted_new_username):
            print("This user already exists, please add a non-exisiting user")
            continue

        inputted_new_password = input("Please enter a new password: ")
        second_password = input("Please confirm your password: ")

        # if both entered passwords match, write user info to users.txt and exit while loop, else ask to try again
        if second_password == inputted_new_password:
            with open("user.txt", "a") as f:
                f.write(f"\n{inputted_new_username}, {inputted_new_password}")
            passwords_match = True

        else:
            print("Sorry the password you entered does not match the first, please try again")


def add_task():
    """adds a new task to task.txt file, asks user to input information and writes it to task file"""
    task_to_add = True

    while task_to_add:
        inputted_task_assignee = input("Please enter username of the person whom the task is assigned to: ")
        inputted_task_title = input("Please enter title of the task: ")
        inputted_description = input("Please enter description of the task: ")
        inputted_due_date = input("Please enter due date of task - in the form MMM-DD-YYYY: ")
        today_date = date.today().strftime("%b-%d-%Y")
        task_complete = "No"

        output = f"{inputted_task_assignee}, {inputted_task_title}, {inputted_description}, " \
                 f"{inputted_due_date}, {today_date}, {task_complete}"

        with open("tasks.txt", "a") as f:
            f.write(f"\n{output}")

        more_tasks = input("Would you like to add another task? y or n? ")
        if more_tasks == "n":
            task_to_add = False


def write_tasks(list, position):
    "takes in a list of tasks and position, concantinates string of task information including position, and prints it"
    output = f"------------{position}------------\n"
    output += f"Username: {list[0]}\n"
    output += f"Task title: {list[1]}\n"
    output += f"Task description: {list[2]}\n"
    output += f"Date due: {list[3]}\n"
    output += f"Date assigned: {list[4]}\n"
    output += f"Task complete? {list[5]}\n"
    output += f"-------------------------\n"
    print(output)


def view_all():
    """reads tasks and prints out in readable format"""
    with open("tasks.txt", "r") as f:
        data = f.readlines()

    # cycle through task data, split each line into a list where each list item is a different piece of
    # information, e.g. due date, task name etc. Print these tasks in readable format
    for pos, line in enumerate(data, 1):
        split_data = line.split(", ")
        write_tasks(list=split_data, position=pos)


def edit_username(task_data, task_number):
    """takes in task data and a specific task number. Allows user to edit assigned user in specified task.
    Returns new data in string format"""
    new_data = []
    for pos, line in enumerate(task_data, 1):

        if pos == int(task_number):
            split_line = line.split(", ")
            split_line[0] = input("Enter a new user ")
            print(f"Task {task_number} is now assigned to {split_line[0]}")
            new_data.append(', '.join(split_line))

        else:
            new_data.append(line)

    return new_data


def edit_due_date(task_data, task_number):
    """takes in task data and a specific task number. Allows user to edit assigned user in specified task. 
        Returns new data in string format"""
    new_data = []
    for pos, line in enumerate(task_data, 1):

        if pos == int(task_number):
            split_line = line.split(", ")
            split_line[4] = input("Enter a new due date - in the form MMM-DD-YYYY: ")
            print(f"Task {task_number} now has a due data of {split_line[4]}")
            new_data.append(', '.join(split_line))

        else:
            new_data.append(line)

    return new_data


def mark_task_as_complete(task_number, task_data):
    """takes in task number and task data and marks specified task as complete. Returns new task data"""
    new_data = []
    for pos, task in enumerate(task_data, 1):
        if pos == int(task_number):
            edited_task = task.replace("No", "Yes")
            new_data.append(edited_task)
            print(f"Task{task_number} is now marked as complete")

        else:
            new_data.append(task)

    return new_data


def view_mine(user):
    """takes in user argument and prints out user tasks in readable format. Allows user to edit incomplete
    tasks by changing assignee or due date"""
    completed_tasks = []  # initialise empty list to append completed task numbers to

    with open("tasks.txt", "r") as f:  # open tasks and save data as list of lines
        data = f.readlines()

    for pos, line in enumerate(data, 1):  # use enumerate to give each task a number
        split_data = line.split(", ")  # split each line into a list of separate pieces of info, e.g. title, date etc.
        if "Yes" in line:
            completed_tasks.append(pos)  # if task is complete, add the task number to the list of completed tasks

        if split_data[0] == user:  # if the assignee is the same as the user, print their tasks
            write_tasks(list=split_data, position=pos)

    # editing tasks
    task_to_edit = input("Would you like to edit a task? If yes, type the task "
                         "number that you want to edit, or type -1 to return to main menu: ")
    if task_to_edit == "-1":  # if the user selects -1, take them back to the main menu
        return

    #  task selection checks
    selected_task = False
    while not selected_task:  # continually ask user to edit a task until they input a task which is not complete

        # check if entered task number represents a completed task, if task is incomplete, break out of while loop
        if int(task_to_edit) in completed_tasks:
            print("Sorry can't edit a complete task")
            task_to_edit = input("Enter the task number of the task you would like to edit: ")
        else:
            selected_task = True

    # ask user what they want to edit
    complete_or_edit = input(f"Would you like to mark task{task_to_edit} as complete (c) or edit (e) the task? ")

    if complete_or_edit == "c":
        # mark task as complete
        edited_data = mark_task_as_complete(task_number=task_to_edit, task_data=data)

    else:
        user_or_date = input("Would you like to edit user assigned (type user) or due date? (date) ")
        if user_or_date == "user":
            # edit username
            edited_data = edit_username(task_data=data, task_number=task_to_edit)

        else:
            # edit due date
            edited_data = edit_due_date(task_data=data, task_number=task_to_edit)

    #join together list of tasks into 1 big string
    string_data = ''.join(edited_data)

    with open("tasks.txt", "w+") as new_file:
        new_file.write(string_data)

    return


def disp_stats():
    """reads tasks and user text docs and returns a string displaying number of users and number of tasks"""
    with open("tasks.txt", "r") as tasks:
        num_tasks = len(tasks.readlines())

    with open("user.txt", "r") as users:
        num_users = len(users.readlines())

    output = f"------------STATISTICS-------------\n"
    output += f"Number of users: {num_users}\n"
    output += f"Number of tasks: {num_tasks}\n"
    output += f"\n"

    return output


def login():
    """asks user for username and password, if in user db, logins in, else gives relevant error message adn option
    to try again"""
    entered_username = username.get()
    entered_password = password.get()

    if entered_password not in passwords and entered_username not in usernames:
        messagebox.showinfo("Incorrect Credentials", "These are both not in our system")
        return True

    for i in range(len(usernames)):
        if entered_username == usernames[i] and not entered_password == passwords[i]:
            messagebox.showinfo("Incorrect Credentials", "Your password is incorrect try again")
            return True

        if entered_password == passwords[i] and not entered_username == usernames[i]:
            messagebox.showinfo("Incorrect Credentials", "Your username is incorrect try again")
            return True

        if entered_username == usernames[i] and entered_password == passwords[i]:
            messagebox.showinfo("Login Successful", "Please wait while we log you in!!")
            tkWindow.destroy()
            return False


def generate_task_overview():
    """prints task data: total tasks, total complete / incomplete tasks, total overdue, names of overdue, percentage
    overdue, percentage complete"""
    with open("tasks.txt", "r") as f:
        task_data = f.readlines()
    # total num
    total_tasks = len(task_data)

    # total complete
    complete_tasks = [task for task in task_data if "Yes" in task]
    num_complete_tasks = len(complete_tasks)

    # total incomplete
    incomplete_tasks = [task for task in task_data if "No" in task]
    num_incomplete_tasks = len(incomplete_tasks)

    # total overdue
    num_overdue = 0
    task_due = ""
    for task in incomplete_tasks:
        split_data = task.split(",")
        if split_data[4].strip(" ") < date.today().strftime("%b-%d-%Y"):
            num_overdue += 1
            task_due += split_data[1] + ", "

    # percentage incomplete
    percentage_incomplete = round(100 * num_incomplete_tasks / total_tasks)

    # percentage overdue
    percentage_overdue = round(100 * num_overdue / total_tasks)

    output = f"------------TASK OVERVIEW------------"
    output += f"Total complete tasks: {str(num_complete_tasks)}\n"
    output += f"Total incomplete tasks: {str(num_incomplete_tasks)}\n"
    output += f"Total overdue tasks: {str(num_overdue)}\n"
    output += f"The overdue tasks are: {task_due}\n"
    output += f"Percentage incomplete: {str(percentage_incomplete)}%\n"
    output += f"Percentage overdue: {str(percentage_overdue)}%"

    return output


def generate_user_overview(user):
    with open("user.txt", "r") as f:
        user_data = f.readlines()
    # total num users
    total_users = len(user_data)

    # total num tasks
    with open("tasks.txt", "r") as f:
        task_data = f.readlines()
    total_tasks = len(task_data)

    # total tasks for that user
    user_tasks = [task for task in task_data if user in task]
    num_user_tasks = len(user_tasks)

    # percentage tasks for user
    percentage_user_tasks = round(100 * num_user_tasks / total_tasks)

    # percentage user tasks completed
    completed_user_tasks = [user_task for user_task in user_tasks if "Yes" in user_task]
    num_completed_user_tasks = len(completed_user_tasks)
    percentage_completed_user_tasks = round(100 * num_completed_user_tasks / num_user_tasks)

    # percentage user tasks not yet completed
    percentage_incomplete_user_tasks = 100 - percentage_completed_user_tasks

    # percentage incomplete and overdue
    incomplete_user_tasks = [user_task for user_task in user_tasks if "No" in user_task]
    num_overdue = 0
    tasks_due = ""

    for task in incomplete_user_tasks:
        split_task = task.split(",")
        if split_task[4].strip(" ") < date.today().strftime("%b-%d-%Y"):
            num_overdue += 1
            tasks_due += split_task[1] + ", "

    percentage_overdue = round(100 * num_overdue / num_user_tasks)

    output = f"------------USER OVERVIEW------------\n"
    output += f"Total tasks for {user}: {str(num_user_tasks)}\n"
    output += f"Percentage of {user}'s tasks out of total tasks: {str(percentage_user_tasks)}%\n"
    output += f"Percentage of {user}'s tasks that have been completed: {str(percentage_completed_user_tasks)}%\n"
    output += f"Percentage of {user}'s tasks that are not yet complete: {str(percentage_incomplete_user_tasks)}%\n"
    output += f"Percentage of {user}'s tasks that are not yet complete and overdue: {str(percentage_overdue)}%\n"
    output += f"The incomplete and overdue tasks are: {tasks_due}\n"

    return output


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
tkWindow.title('Task Manager Login')
tkWindow.config(padx=20, pady=20)

# username label and text entry box
Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()  # holder for string variables
Entry(tkWindow, textvariable=password).grid(row=1, column=1)

# login button
Button(tkWindow, text="Login", command=login).grid(row=2, column=0, columnspan=2, sticky="EW")

tkWindow.mainloop()
inputted_username = username.get()
inputted_password = password.get()

# ========choose option section ==========

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if inputted_username == "admin":

        # # set up tk window
        # tkWindow = Tk()
        # tkWindow.geometry('250x250')
        # tkWindow.title('Admin Options')

        menu = input(admin_menu()).lower()

    else:
        menu = input(user_menu()).lower()

    # add a new user to the user.txt file
    if menu == 'r':
        reg_user()  # register user

    # add task
    elif menu == 'a':
        add_task()

    # print all tasks in readable format
    elif menu == 'va':
        view_all()

        # print just users tasks
    elif menu == 'vm':
        view_mine(inputted_username)

    # add stats to reports
    elif menu == "s":
        # write stats to task overview file
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write(disp_stats() + generate_task_overview())

        # write stats to user overview file
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write(disp_stats() + generate_user_overview(inputted_username))
        disp_stats()

    # generate reports
    elif menu == "gr":
        # write to task overview file
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write(generate_task_overview())

        # write to user overview file
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write(generate_user_overview(inputted_username))

    # exit the code
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
