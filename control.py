age = int(input("what age are you? "))  # asks user to input age

if age >= 18:
    print("Congrats you are old enough")  # prints this if age over or equal to 18
elif age > 16:
    print("almost there!")  # prints this if age over 16 but under 18
else:
    print("You're just too young")  # prints this if age below 16
