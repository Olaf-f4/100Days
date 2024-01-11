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

NATO_open = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO = pandas.DataFrame(NATO_open)
print(NATO)

NATO_Dict = {index: row for (index, row) in NATO.iterrows()}
print(NATO_Dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

