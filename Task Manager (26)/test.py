from datetime import date
#
# with open("tasks.txt", "r") as f:
#     data = f.readlines()
#
# for line in data:
#     if "Yes" in line:
#         print(line)
#
# uncompleted_tasks = [line for line in data if "No" in line]
# print(uncompleted_tasks)

today_date = date.today().strftime("%b-%d-%Y")
print(today_date)

if today_date < "Dec-30-2022":
    print("not overdue")

if "Dec-29-2022" > "Jan-07-2023":
    print("true")
else:
    print("false")

