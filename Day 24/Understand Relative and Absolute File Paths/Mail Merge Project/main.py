# TODO: Create a letter using starting_letter.txt
# for each name in names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()  # Loop through the name and strip the new line
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Create a new file with a unique name for each iteration and provide the file extension
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            # Write the modified content to the new file
            completed_letter.write(new_letter)
