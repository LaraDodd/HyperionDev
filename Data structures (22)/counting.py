sentence = "Hello my name is Rumple Stilkskin and I am an imp"

# sentence manipulation
split_sentence = sentence.lower().split(" ") # make all chars lower and split sentence to a list of words
sentence_without_spaces = "".join(split_sentence) # join list into one string with no spaces

# create empty dictionary to add to
char_dict = {}

# cycle through each char and if in the dictionary, add char as key and 1 as value, else add 1 to value
for char in sentence_without_spaces:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1

print(char_dict)