#  initialise full_name boolean
full_name = False

while not full_name:
    # ask user to input name
    name = input("Please enter your full name ")

    #  check that 2 words in name
    if len(name) == 0:
        print("You've not entered anything, try again")
    elif not " " in name:
        print("You have not entered 2 words, try again")
    elif len(name) <= 4:
        print("You've only entered 4 characters, make sure this is your first and second name")
    elif len(name) > 25:
        print("You've entered more than 25 characters. Please make sure you have only entered you full name")
    else:
        full_name = True

print("Thanks for entering your name")