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
#
# today_date = date.today().strftime("%b-%d-%Y")
# print(today_date)
#
# if today_date < "Dec-30-2022":
#     print("not overdue")
#
# if "Dec-29-2022" > "Jan-07-2023":
#     print("true")
# else:
#     print("false")
#
list = [[3]*7 for item in range(7)]

for row in list:
    print(row)

for i in range(1,len(list)-1):
    new_list_row = list[i]
    new_list= new_list_row[1:6]
    print(new_list)

print()

for row in newlist:
    print(row)
