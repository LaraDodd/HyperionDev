'''This program contains string manipulation techniques'''

str_manip = input("Please input a sentence ")

str_manip_length = len(str_manip)  # finding length of str_manip
print(str_manip_length)

last_letter = str_manip[-1]  # getting the final char in string
print(last_letter)

new_string = str_manip.replace(last_letter, "@")  # replacing all instances of the final char with '@'
print(new_string)

last_3_backwards = str_manip[-1:-4:-1] # get last 3 chars of sentence and then reverse them
print(last_3_backwards)

five_letter_word = str_manip[:3]+str_manip[-2:]  # concatenating first 3 and last 2 chars in sentence
print(five_letter_word)

split_sentence = str_manip.split(" ")
for word in split_sentence:
    print(word)

