# initial variables
john_entered = False  # initialise bool
names = []  # initialise names list

while not john_entered:
    user_input = input("Please enter a name ").lower()

    if user_input == "john":  # if user enters john, exit while loop and do not append john to the list
        john_entered = True
        continue

    user_input = user_input.title().strip(" ")  # Title case the names and remove the spaces if any
    names.append(user_input)  # append name to names list

print(names)
