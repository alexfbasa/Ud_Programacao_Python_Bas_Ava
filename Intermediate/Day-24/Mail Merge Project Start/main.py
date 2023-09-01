# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read()
    names_ordered = name_list.split()
    print(names_ordered)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

for name in names_ordered:
    new_letter = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as file:
        if file.write(new_letter):
            print(f"Letter for {name} created. ")
