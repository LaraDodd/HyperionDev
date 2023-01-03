import pyjokes
import random

"""generate list of jokes in text file"""
# using get_jokes() to generate a whole list of jokes
list_of_jokes = pyjokes.get_jokes(language="en", category="all")

# write jokes to separate txt doc
with open("jokes.txt", "w") as jokes:
    for joke in list_of_jokes:
        jokes.write(f"{joke}\n")

"""main code of creating list of jokes"""
# create list of jokes
jokes_list = []
with open("jokes.txt", "r") as jokes:
    for line in jokes:
        jokes_list.append(line)


# creating a function to generate joke
def generate_rand_joke():
    rand_joke = random.choice(jokes_list)
    print(rand_joke)


# calling function
generate_rand_joke()
