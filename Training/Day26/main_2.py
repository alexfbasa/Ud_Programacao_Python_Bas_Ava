import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Type a word: ").upper()

output_phonetic_dict = [data_dic[letter] for letter in word]

print(output_phonetic_dict)
