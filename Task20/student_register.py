no_students = int(input("How many students are in the class? "))
student_id_list = []

# cycle through loop and add every student id to a list
for student in range(no_students):
    student_id = input("Please enter student ID ")
    student_id_list.append(student_id)

# open a new document called reg form and add each student to it
with open("reg_form.text", "w+") as f:
    for stud_id in student_id_list:
        f.write("Student ID: " + str(stud_id) + "\n")
