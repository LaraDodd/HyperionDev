import pandas

df = pandas.read_txt("input.txt")
print(df)

with open("input.txt", "r") as file:
    input_data = file.readlines()

split_list = [line.split(":") for line in input_data]

print(split_list)

