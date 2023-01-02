from tkinter import *
from tkinter import messagebox


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

# ask user to enter username and password
# while True:

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



