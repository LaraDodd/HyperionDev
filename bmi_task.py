#  ask user to input height and weight
height = float(input("Please enter your height (m): "))
weight = float(input("Please enter your weight (kg): "))

#  calculate bmi
bmi = round((weight / height**2),2)

print(f"Your bmi is {bmi}")

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")