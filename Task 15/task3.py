"""while loop count down from 20"""
# initialise number
number = 20

#print number whilst it is greater than or equal to 0, reduce number each iteration
while number >= 0:
    print(number)
    number -= 1


"""loop which displays even numbers between 1 and 20"""
for number in range(2,20,2):
    print(number)


"""increasing * print"""
string = ""

for i in range(5):
    string += "*"
    print(string)

"""GDC of 2 numbers"""
#  setting initial variables
gcd_found = False
factors2 = []
factors1 = []

# ask user to enter 2 numbers
user_input_1 = 1238
user_input_2 = 83

#iterate through all integers between and including 1 and entered number, check if integer is a factor
for i in range(1, user_input_1+1):
    if user_input_1 % i == 0:
        factors1.append(i)

#repeat for second input
for i in range(1, user_input_2+1):
    if user_input_2 % i == 0:
        factors2.append(i)

#while gdc not found, find max of one list and check if that number is in other, if it isn't, remove it from list
while not gcd_found:
    max_factor1 = max(factors1)
    if max_factor1 not in factors2:
        factors1.remove(max_factor1)
    else:
        print(f"GCD = {max_factor1}")
        gcd_found = True

