"""this program keeps asking the user to enter a number until they enter -1,
it then prints an average of all the numbers they inputted, excluding -1"""

#  initialise numbers list and user_input
numbers = []
user_input = None

#  ask user to enter a number and add the number to the numbers list, until they enter -1
while user_input != -1:
    user_input = int(input("Please enter a number "))
    if user_input == -1:
        break
    numbers.append(user_input)

#  calculate the average of the numbers in the list
average = sum(numbers) / len(numbers)

# print the average
print(f"The average of the numbers is {round(average, 2)}")
