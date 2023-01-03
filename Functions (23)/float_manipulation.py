"""this program asks user for 10 numbers anf finds the: total, max, min, average and median"""

import math

numbers = [-5, -5, -3, -4, 0, -1]
float_numbers = [float(element) for element in numbers]  # list comprehension: recast all numbers to floats

# find total
total = sum(numbers)
print(f"total of all numbers: {total}")

# find index of the maximum
max_num = max(float_numbers)  # find max number

for pos, number in enumerate(float_numbers):  # use enumerate to track index, find index of max num
    if max_num == number:
        max_num_index = pos

print(f"index of maximum value: {max_num_index}")

# find index of the minimum
min_num = min(float_numbers)  # find min number

for pos, number in enumerate(float_numbers):  # use enumerate to track index, find index of min num
    if min_num == number:
        min_num_index = pos

print(f"index of minimum value: {min_num_index}")

# calculate the average
ave_num = round(sum(float_numbers)/len(float_numbers), 2)
print(f"average of all numbers: {ave_num}")

# calculate the median (without importing statistics)
#if even, find the 2 indexes by diving length by 2 and taking the number below result as well
if len(float_numbers) % 2 == 0:
    index1 = int(len(float_numbers)/2)
    index2 = index1 - 1
    median = (sorted(float_numbers, key=float)[index1] + sorted(float_numbers, key=float)[index2])/2

# if odd, find index by dividing length by 2 and rounding down
else:
    index1 = int(round(len(float_numbers)/2, 1))
    print(index1)
    median = (sorted(float_numbers, key=float)[index1]) # sort the list into increasing value

print(f"the median is: {median}")