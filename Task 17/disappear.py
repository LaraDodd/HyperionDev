"""this program removes specific characters from a sentence, as dictacted by the user"""
chars_to_remove = []  # initialise chars to remove list to add to later
edited_words_list = []  # initialise edited words list to add to later
more_letters = True  # initialise bool for while loop

user_sentence = input("Please input a random sentence ").lower()
user_sentence_word_list = user_sentence.split(" ")  # create a list of all the words in the sentence

#  ask user to input a char, add char to 'chars to remove' list, until they enter 'finish', after which, exit while loop
while more_letters:
    user_char = input("Enter a letter you would like to remove from your sentence. Type 'finish' when done ")
    if user_char.lower() == "finish":
        more_letters = False
        continue
    chars_to_remove.append(user_char)

#  for each word in user sentence word list, iterate through chars to remove, replace the chars in word with nothing
for word in user_sentence_word_list:
    for char in chars_to_remove:
        word = word.replace(char, "")

    edited_words_list.append(word)  # append the new edited word to the edited words list

edited_user_sentence = " ".join(edited_words_list)  # join together each word in word list, with space between each
print(edited_user_sentence)
