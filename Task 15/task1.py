"""this program displays the times table of any number"""

#  ask user to enter a number
user_input = int(input("Please enter a number "))

print(f"The {user_input} times table is:")

#  iterate through integers from 1 to and including 12, multiply by user input, print answer
for num in range(1, 13):
    answer = num * user_input
    print(f"{user_input} x {num} = {answer}")
