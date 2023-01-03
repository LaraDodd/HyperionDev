# days of the week function
def days_of_week():
    """this function prints out all the days of the week"""
    print("Monday,\nTuesday,\nWednesday,\nThursday,\nFriday,\nSaturday,\nSunday")


# hello function
def hello_sentence_edit(string):
    """this function takes in a sentence and replaces every second word with the word hello"""
    words_list = string.split(" ")  # split sentence into list of words

    for index in range(len(words_list)):
        if index % 2 == 0:
            words_list[index] = "hello"  # replace every other word with hello

    edited_sentence = ' '.join(words_list)  # join words up into one sentence with space in between
    return edited_sentence


# call the functions
days_of_week()
print(hello_sentence_edit("The quick brown fox jumped over the lazy dog"))
