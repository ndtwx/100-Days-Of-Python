import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
"""
<[phonetic_dict[letter]>
Use the square brackets and then pass in the letter to go through the phonetic dictionary 
and pick out the value that corresponds to the particular letter  
"""


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in word]
        # new list = [new_item for item in list]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()
