import math

print("investment - to calculate the amount of interest you'll earn on your investment\n"
      "bond       - to calculate the amount you'll have to pay on a home loan")

#  ask user to choose bond or investment
calculation_choice = input("Enter either 'investment' or 'bond' from the menu to proceed: ").lower()

if calculation_choice == "investment":
    # ask user for inputs
    amount = float(input("Enter the amount of money deposited in pounds "))

    interest = input("Enter the interest rate as a percentage ")
    if "%" in interest:
        interest = interest.strip("%")  # strip out % if accidentally entered with it
    interest = float(interest) / 100  # converting percentage to decimal

    years = float(input("Enter the number of years you want to invest for "))

    interest_type = (input("Do you want 'simple' or 'compound' interest? "))

    #  calculation of total based on interest type
    if interest_type == "simple":
        total = amount * (1 + interest * years)
    else:
        total = amount * math.pow(1 + interest, years)

    # display result
    print(f"total amount after interest: {round(total, 2)}")

elif calculation_choice == "bond":
    # ask user for inputs
    value = float(input("Enter the avlue of house in pounds "))

    interest = input("Enter the interest rate as a percentage ")
    if "%" in interest:
        interest = interest.strip("%")
    interest = float(interest) / 100  # converting percentage to decimal
    monthly_interest = interest / 12

    months = float(input("Enter the number of months you plan to repay the bond over "))

    # calculate repayment
    repayment = (monthly_interest * value) / (1 - (1 + monthly_interest) ** (-months))

    # display result
    print(f"total repayment per month: {round(repayment, 2)}")
