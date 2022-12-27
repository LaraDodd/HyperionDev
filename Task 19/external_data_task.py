#  initialise names and DOB lists
names = []
birthdays = []

#  read in external data
with open('DOB.txt', 'r+') as f:  # open DOB.txt as a read and edit
    for line in f:  # cycle through each line in the text document
        line = line.strip("\n")  # remove all the '\n' from the end of birthdays
        name_birthday_split_list = line.split(" ")  # create a list where each item is a word in the line
        name = " ".join(name_birthday_split_list[0:2])  # join the first 2 items in the list into one string
        names.append(name)  # append to names list
        birthday = " ".join(name_birthday_split_list[2:]) # join the final 3 items in the list into one string
        birthdays.append(birthday)  # append to birthdays list

print("\033[1m" + "Names:")  # print names in bold
for name in names:  # cycle through names list and print each item
    print("\033[0m" + name)

print("\n")

print("\033[1m" + "Birthdays:")  # print birthdays in bold
for birthday in birthdays:  # cycle through birthdays list and print each item
    print("\033[0m" + birthday)
