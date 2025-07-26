# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

FILE_NAMES = "Input/Names/invited_names.txt"
FILE_LETTER = "Input/Letters/starting_letter.txt"
FILE_OUTPUT_PATH = "Output/ReadyToSend/"

# get names
with open(FILE_NAMES) as file:
    names = file.readlines()
    names = [name.strip('\n') for name in names]

# get letter
with open(FILE_LETTER) as file:
    letter = file.read()

# cycle
for name in names:
    new_letter = letter.replace("[name]", name)
    filename = f"{FILE_OUTPUT_PATH}{name}.txt"
    
    with open(filename, mode="w") as file:
        file.write(new_letter)
