int1 = int(input("Please input a number "))
int2 = int(input("Please input a number "))
int3 = int(input("Please input a number "))

sumtotal = int1+int2+int3

print(f"The sum is {sumtotal}")

print(f"The first number minus the second is {int1-int2}")

print(f"The third number multiplied by the first is {int1*int3}")

print(f"The sum of all 3 numbers divided by the third number is {round(sumtotal/int3,3)}")
