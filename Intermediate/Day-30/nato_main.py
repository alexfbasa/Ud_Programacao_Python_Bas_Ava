import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_to_dict = {row.letter: row.code for (letter, row) in data.iterrows()}


def switch_to_nato():
    word = input("Enter a word:").upper()
    try:
        output = [data_to_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        switch_to_nato()
    else:
        print(output)


switch_to_nato()
