# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")  # added paranethesis to all print functions
print("\n")

ageStr = "24 years old"  # I'm 24 years old.
age = int(ageStr[:2])  # sliced string to just get 24, then turned into an integer
print("I'm " + str(age) + " years old.")  # turned age to string, so it could be concatenated with the strings
three = "3"

answerYears = age + int(three)  # added integer to this

print(f"The total number of years: {answerYears}")  # turned this print to f-string
answerMonths = answerYears * 12  # changed answer to answerYears
print("In 3 years and 6 months, I'll be " + str(answerMonths + 6) + " months old")  # added 6 to the total months

# HINT, 330 months is the correct answer
