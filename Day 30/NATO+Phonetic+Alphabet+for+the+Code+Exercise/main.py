# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 30/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

run_code = True
while run_code:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError as error_key:
        print(f"Sorry, Only letter/ alphabets please not {error_key}")
    else:
        run_code= False    
        
