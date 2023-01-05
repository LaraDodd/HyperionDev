def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # changed k to key


simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh",  # ' in d'oh messed up string, rewrote
                         "maggie": "(Pacifier Suck)"  # removed space
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])  # keys weren't passed in as a list, changed
