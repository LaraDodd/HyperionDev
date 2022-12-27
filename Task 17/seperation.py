"""This program takes a sentence a prints each word on a separate line"""

user_sentence = input("Please input a random sentence ")

user_sentence_words_list = user_sentence.split(" ")

for word in user_sentence_words_list:
    print(word)