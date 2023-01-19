# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    names_list = names.read().split()

with open("Input/Letters/starting_letter.txt") as letter:
    content_letter = letter.read()


for name in names_list:
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        new_content = content_letter.replace(f"[name]", name)
        file.write(new_content)
