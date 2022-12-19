str_manip = input("Please input a sentence ")

last_letter = str_manip[-1]  # getting the final char in string
print(last_letter)

new_string = str_manip.replace(last_letter, "@")  # replacing all instances of the final char with '@'
print(new_string)

last_3_backwards = str_manip[-3:][::-1]  # get last 3 chars of sentence and then reverse them
print(last_3_backwards)

five_letter_word = str_manip[:3]+str_manip[-2:]  # concantinating first 3 and last 2 chars in sentence
print(five_letter_word)
