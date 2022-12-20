user_integer = int(input("Please enter a number "))

if user_integer % 5 == 0 and user_integer % 2 == 0:
    print("divisible by 5 and 2")
elif user_integer % 5 == 0 or user_integer % 2 == 0:
    print("divisible by 5 or 2")
else:
    print("not divisible by 5 or 2")