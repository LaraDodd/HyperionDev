"""this program asks user to enter a number and prints out all the even numbers between 1 and
possibly including that number"""

user_input = int(input("Please enter a number "))

#  initialise counter
counter = 1

#  cycle through all numbers between 1 and input and print out even numbers
while counter <= user_input:
    if counter % 2 == 0:
        print(counter)
    counter += 1
