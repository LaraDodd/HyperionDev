
integers = []

with open("numbers1.txt", "r+") as f1:
    for line in f1:
        integers.append(int(line))

with open("numbers2.txt", "r+") as f2:
    for line in f2:
        integers.append(int(line))

integers.sort()

with open("all_numbers.txt", "w+") as f3:
    for integer in integers:
        f3.write(f"{integer} \n")