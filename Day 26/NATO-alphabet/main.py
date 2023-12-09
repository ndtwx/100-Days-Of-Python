import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass



student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row. code for (index,row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
"""
<[phonetic_dict[letter]>
Use the square brackets and then pass in the letter to go through the phonetic dictionary 
and pick out the value that corresponds to the particular letter  
"""
word = input("Enter a word: ").upper()
# new list = [new_item for item in list]
new_list = [phonetic_dict[letter] for letter in word]

print(new_list)
