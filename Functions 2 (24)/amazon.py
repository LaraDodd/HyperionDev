def min(list):
    """returns minimum value from a list"""
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min


def max(list):
    """returns max value from a list"""
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max


def ave(list):
    """returns average value from a list"""
    sum = 0
    for num in list:
        sum += int(num)
    average = sum / len(list)
    return average


def create_list(string):
    """creates a list from a string of chars separated by a comma"""
    string.strip("\n")
    list = string.split(",")
    return list


with open("input.txt", "r") as file:
    input_data = file.readlines()

# strip data of extra symbols and new line chars
stripped_data_list = [line.strip('\nï»¿') for line in input_data]

# separate each item in the list to min/max/avg and a list of numbers
split_list = [line.split(":") for line in stripped_data_list]

# initialise output
output = ""

# turn each sequence into lists and find the max, min and avg
for sub_list in split_list:
    new_list = create_list(sub_list[1])

    if sub_list[0] == "min":
        output += f"minimum of {new_list} is {min(new_list)}\n"
    elif sub_list[0] == "max":
        output += f"maximum of {new_list} is {max(new_list)}\n"
    elif sub_list[0] == "avg":
        output += f"average of {new_list} is {ave(new_list)}"

# write to output file
with open("output.txt", "w") as o_file:
    o_file.write(output)
