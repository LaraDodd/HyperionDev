import random

# col_no = 5
# row_no = 3
#
# array = [ [None] * col_no for _ in range(row_no)]
# print(array)

new_array = [[random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(5)]
print(new_array)

counter = 1
for row in new_array:
    print(f"term {counter}")
    counter += 1
    for col in row:
        print(col, end=f"% ")
    print()


new_array1 = [[random.randint(1, 10) for num in range(random.randint(1, 4))] for i in range(5)]
print(new_array1)

row_no = 1
for row in new_array1:
    no_col = len(row)
    print(f"no. cols in row {row_no} is {no_col}")
    row_no += 1
    for col_item in row:
        print(f"col item: {col_item}")


