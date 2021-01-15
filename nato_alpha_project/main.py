import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

pa_dict = {row.letter: row.code for (row, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [pa_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
