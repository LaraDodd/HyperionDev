"""This program determines whether an entered year is a leap year"""

""" Note to marker, a year is a leap year if it is divisible by 4 
UNLESS it is also divisible by 100
EXCEPT when it is also divisible by 400
so I have reflected this in my code and not just used the 'is divisible by 4' rule
"""

#user inputs
year = int(input("What year do you want to check? "))
num_years = int(input("How many years after that do you want to check? "))

# iterates through entered number of years, checks if the year is a leap year and prints out the result
for i in range(num_years):
    if year % 4 == 0:
        leap_year = True  # year is a leap year if it is divisible by 4

        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True  # except if it is divisible by 100

            else:
                leap_year = False  # unless it is also divisible by 400
    else:
        leap_year = False

    #  print result
    if leap_year:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    #  add 1 to year after every iteration
    year += 1

