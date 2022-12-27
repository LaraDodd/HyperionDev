"""this program reads in a string and makes each alternative char upper case.
It then makes each alternative word uppercase"""

user_str = input("Please input a random sentence ")

"""Task 1"""
user_str_word_list = user_str.split(" ")  # split string into list of words

edited_str_list = []  # initialise list to append to once edits have been made

for word in user_str_word_list:
    word = list(word)  # change word to list of chars (strings are immutable so can't edit individual elements of them)
                       # note to marker: please could you explain this a bit further?
    for index in range(len(word)):
        if index % 2 == 0:
            word[index] = word[index].upper()  # make upper if index is even
        else:
            word[index] = word[index].lower()  # make lower if index is odd

    word_str = "".join(word)  # change word list back into a string
    edited_str_list.append(word_str)  # append new edited word to a list

new_sentence = " ".join(edited_str_list)  # join all edited words together into a string, separating each with a space
print(new_sentence)

"""Task 2"""
edited_word_list = []  # initialise list to append edited words to later

for index in range(len(user_str_word_list)):

    if index % 2 == 0:
        edited_word = user_str_word_list[index].upper()  # if index is even, make word upper
    else:
        edited_word = user_str_word_list[index].lower()  # if index is odd, make word lower

    edited_word_list.append(edited_word)  # add edited word to the list

new_sentence_2 = " ".join(edited_word_list)  # join list of words into a string, each word separated with space
print(new_sentence_2)

