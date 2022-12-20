# set variables
num1 = 4
num2 = 9
num3 = 6

# compare num1 and num2 and display larger value
if num1 > num2:
    print(f"num1 ({num1}) is bigger")
else:
    print(f"num2 ({num2}) is bigger")

# determine whether num1 is odd
if num1 % 2 == 0:
    print("num1 is even")
else:
    print("num1 is odd")

# sort numbers biggest to smallest
numbers_list = [num1, num2, num3]
numbers_list.sort()
print(numbers_list)
