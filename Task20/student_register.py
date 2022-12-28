no_students = 20
student_id_list = []

for student in range(no_students):
    student_id = input("Please enter student ID ")

with open("reg_form.text", "w+") as f:
    for stud_id in student_id_list:
        f.write(stud_id+"\n")

