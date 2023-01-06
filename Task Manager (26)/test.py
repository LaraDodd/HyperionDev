with open("tasks.txt", "r") as f:
    data = f.readlines()

for line in data:
    if "Yes" in line:
        print(line)

uncompleted_tasks = [line for line in data if "No" in line]
print(uncompleted_tasks)

