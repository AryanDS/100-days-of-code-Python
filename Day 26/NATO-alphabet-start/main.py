student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


##########
import pandas as pd

df = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(df)

# for index, row in df.iterrows():
#     nato_dict[row.letter] = row.code

nato_dict= {row.letter: row.code for index, row in df.iterrows()}

user_input= input("Please enter a word: ").upper()

output = [nato_dict[i] for i in user_input]
print(output)


#output=[value for key,value in nato_dict if key in user_split]
output_1=[nato_dict[key] for key in nato_dict if key in list(user_input)]
print(output_1)
