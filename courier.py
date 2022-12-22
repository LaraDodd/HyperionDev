"""This code calculates the cost of sending a parcel"""


package_price = input("Please can you enter the total cost of the package? (in R) ")
if "£" in package_price:
    package_price = float(package_price.strip("£"))

distance = float(input("Please can you enter the total distance of the delivery in kms? "))

#  ask user if they would like air or freight?
air_freight = input("Would you like air or freight delivery method? ").lower()

#  ask user if they would like full or half insurance?
insurance_type = input("Would you like full insurance of half insurance? ").lower()

#  ask user if they would like it gift wrapped
gift_wrap = input("Would you like it gift wrapped? yes or no? ").lower()

#  ask user if they would like priority or standard delivery
priority_standard = input("Would you like priority or standard delivery? ").lower()

if air_freight[0] == "f":  # if the first letter of air_freight string is f (due to user inputting freight)
    cost_per_km = 0.25
elif air_freight[0] == "a":
    cost_per_km = 0.36
else:
    print("error, run code again")

if insurance_type[0] == "f":
    insurance_cost = 50
elif insurance_type[0] == "h":
    insurance_cost = 25
else:
    print("error, run code again")

if gift_wrap[0] == "y":
    gift_cost = 15
elif gift_wrap[0] == "n":
    gift_cost = 15
else:
    print("error, run code again")

if priority_standard[0] == "p":
    shipping_cost = 100
elif priority_standard[0] == "s":
    shipping_cost = 20
else:
    print("error, run code again")

#  sum them up
total_cost = package_price + distance*cost_per_km + insurance_cost + gift_cost + shipping_cost

print(f"Calc is {package_price} + {distance}*{cost_per_km} + {insurance_cost} + {gift_cost} + {shipping_cost} = R{total_cost}")