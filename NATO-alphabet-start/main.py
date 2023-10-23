import pandas


def NATO():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    data_df = pandas.DataFrame(data)
    new_dict = {l.letter : l.code for (index, l) in data.iterrows()}

    word = input("Enter a word. ").upper()
    try:
        phoenics = [new_dict[letter] for letter in word]
    except KeyError:
        print('Please enter alphabets only!')
        NATO()
    else:
        print(phoenics)


NATO()

