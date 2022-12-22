"""this program asks user to enter names of all pupils in a class, the user should indicate
 that all the names have been entered with the word 'stop' """

#  initialising variables
more_students = True
student_names = []

#  while loop which adds user input to a list unless input is 'stop'
while more_students:
    student_name = input(" Please enter the name of a student in your class, "
                         "type 'stop' when you have entered all the students in the class ")
    if student_name.lower() == "stop":
        more_students = False
        break

    student_names.append(student_name)

print(f"The number of students in the class is {len(student_names)}\n"
      f"The students are: {student_names}")
